#
# Copyright (c) 2025, RT-Thread Development Team
#
# SPDX-License-Identifier: Apache-2.0
#
# Change Logs:
# Date           Author       Notes
# 2026-06-25     Codex        add armclang cbuild BSP flow
#
import multiprocessing
import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET


def add_summary(text):
    summary_file = os.getenv('GITHUB_STEP_SUMMARY')
    if summary_file:
        with open(summary_file, 'a', encoding='utf-8') as file:
            file.write(text + '\n')


def run_cmd(cmd, cwd=None, env=None):
    print('\033[1;32m' + cmd + '\033[0m')
    process = subprocess.Popen(
        cmd,
        cwd=cwd,
        env=env,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        errors='replace')

    output = []
    for line in process.stdout:
        output.append(line)
        print(line, end='')

    return output, process.wait()


def check_bsp_build_scripts(bsp_dir):
    missing = []
    for filename in ('SConstruct', 'SConscript'):
        if not os.path.isfile(os.path.join(bsp_dir, filename)):
            missing.append(filename)

    if missing:
        print(f"::error::missing {', '.join(missing)} in {bsp_dir}")
        return False

    return True


def template_uses_ac6(bsp_dir):
    template = os.path.join(bsp_dir, 'template.uvprojx')
    if not os.path.isfile(template):
        print(f"::error::template.uvprojx not found: {template}")
        return False

    try:
        root = ET.parse(template).getroot()
    except ET.ParseError as err:
        print(f"::error::failed to parse {template}: {err}")
        return False

    uac6 = root.find('.//uAC6')
    return uac6 is not None and uac6.text == '1'


def find_solution_file(bsp_dir):
    for filename in ('project.csolution.yml', 'project.csolution.yaml'):
        path = os.path.join(bsp_dir, filename)
        if os.path.isfile(path):
            return filename

    return None


def prepare_pack_root():
    pack_root = os.getenv('CMSIS_PACK_ROOT')
    if not pack_root:
        return True

    os.makedirs(pack_root, exist_ok=True)
    index_file = os.path.join(pack_root, '.Web', 'index.pidx')
    if os.path.isfile(index_file):
        _, res = run_cmd('cpackget update-index')
        return res == 0

    _, res = run_cmd('cpackget init https://www.keil.com/pack/index.pidx')
    return res == 0


def get_ci_scons_args():
    exec_path = os.getenv('RTT_EXEC_PATH')
    if exec_path:
        return f'--exec-path="{exec_path}"'

    return ''


def remove_generated_solution_files(bsp_dir):
    generated_paths = [
        'project.csolution.yml',
        'project.csolution.yaml',
        'project.cproject.yml',
        'project.cproject.yaml',
        'project.cbuild-pack.yml',
        'project.cbuild-set.yml',
        'vcpkg-configuration.json',
        'cbuild-idx.yml',
    ]
    generated_dirs = [
        'out',
        'tmp',
        'outAC6',
    ]

    for name in generated_paths:
        path = os.path.join(bsp_dir, name)
        if os.path.isfile(path):
            os.remove(path)

    for name in generated_dirs:
        path = os.path.join(bsp_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)


def build_bsp_with_cbuild(rtt_root, bsp):
    bsp_dir = os.path.join(rtt_root, 'bsp', bsp)
    if not os.path.isdir(bsp_dir):
        print(f"::error::BSP directory not found: {bsp_dir}")
        return False

    if not check_bsp_build_scripts(bsp_dir):
        return False

    if not template_uses_ac6(bsp_dir):
        print(f"::error::{bsp} does not use AC6 in template.uvprojx")
        return False

    remove_generated_solution_files(bsp_dir)
    scons_args = get_ci_scons_args()

    if os.path.isfile(os.path.join(bsp_dir, 'Kconfig')):
        _, res = run_cmd(f'scons -C bsp/{bsp} --pyconfig-silent {scons_args}'.strip(), cwd=rtt_root)
        if res != 0:
            print(f"::error::pyconfig failed for {bsp}")
            return False

        _, res = run_cmd('pkgs --update-force', cwd=bsp_dir)
        if res != 0:
            print(f"::error::pkgs --update-force failed for {bsp}")
            return False

        _, res = run_cmd('pkgs --list', cwd=bsp_dir)
        if res != 0:
            print(f"::error::pkgs --list failed for {bsp}")
            return False

    _, res = run_cmd(
        f'scons -C bsp/{bsp} --target=mdk5 --project-name=project {scons_args}'.strip(),
        cwd=rtt_root)
    if res != 0:
        print(f"::error::scons --target=mdk5 failed for {bsp}")
        return False

    project_file = os.path.join(bsp_dir, 'project.uvprojx')
    if not os.path.isfile(project_file):
        print(f"::error::project.uvprojx not generated for {bsp}")
        return False

    _, res = run_cmd('uv2csolution project.uvprojx', cwd=bsp_dir)
    if res != 0:
        print(f"::error::uv2csolution failed for {bsp}")
        return False

    solution_file = find_solution_file(bsp_dir)
    if solution_file is None:
        print(f"::error::csolution file not generated for {bsp}")
        return False

    nproc = multiprocessing.cpu_count()
    try:
        _, res = run_cmd(
            f'cbuild {solution_file} --rebuild --packs --toolchain AC6 --output outAC6 --jobs {nproc}',
            cwd=bsp_dir)
        if res != 0:
            print(f"::error::cbuild failed for {bsp}")
            return False

        return True
    finally:
        remove_generated_solution_files(bsp_dir)


if __name__ == '__main__':
    rtt_root = os.getcwd()
    srtt_bsp = [bsp for bsp in os.getenv('SRTT_BSP', '').split(',') if bsp]
    if not srtt_bsp:
        print('::error::SRTT_BSP is empty')
        sys.exit(1)

    if not prepare_pack_root():
        print('::error::failed to prepare CMSIS_PACK_ROOT')
        sys.exit(1)

    failed = 0
    for index, bsp in enumerate(srtt_bsp, start=1):
        print(f"::group::CBuild BSP: =={index}=== {bsp} ====")
        if build_bsp_with_cbuild(rtt_root, bsp):
            add_summary(f'- [OK] cbuild {bsp} success.')
        else:
            add_summary(f'- [FAIL] cbuild {bsp} failed.')
            failed += 1
        print('::endgroup::')

    sys.exit(failed)

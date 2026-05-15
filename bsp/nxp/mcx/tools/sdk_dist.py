import os
import sys
import shutil
cwd_path = os.getcwd()
sys.path.append(os.path.join(os.path.dirname(cwd_path), 'rt-thread', 'tools'))

def get_library_path(BSP_ROOT):
    bsp_family_path = os.path.dirname(BSP_ROOT)
    for library_name in ['libraries', 'Libraries']:
        library_path = os.path.join(bsp_family_path, library_name)
        if os.path.isdir(library_path):
            return library_path, library_name
    return os.path.join(bsp_family_path, 'libraries'), 'libraries'

# BSP dist function
def dist_do_building(BSP_ROOT, dist_dir):
    from mkdist import bsp_copy_files
    import rtconfig

    library_path, library_name = get_library_path(BSP_ROOT)
    library_dir  = os.path.join(dist_dir, library_name)
    print("=> copy bsp drivers")
    bsp_copy_files(os.path.join(library_path, 'drivers'), os.path.join(library_dir, 'drivers'))
    shutil.copyfile(os.path.join(library_path, 'Kconfig'), os.path.join(library_dir, 'Kconfig'))

    # if project Kconfig not exists, no more work to do!
    project_kconfig = os.path.join(dist_dir, 'Kconfig')
    if not os.path.exists(project_kconfig):
        print("project Kconfig not exists!")
        return

    # replace '../libraries/Kconfig' or '../Libraries/Kconfig'
    with open(project_kconfig, 'r') as f:
        data = f.readlines()
    with open(project_kconfig, 'w') as f:
        for line in data:
            line = line.replace('../libraries/Kconfig', library_name + '/Kconfig')
            line = line.replace('../Libraries/Kconfig', library_name + '/Kconfig')
            f.write(line)

#!/bin/bash

#
# Copyright (c) 2024, RT-Thread Development Team
#
# SPDX-License-Identifier: Apache-2.0
#
# Change Logs:
# Date           Author       Notes
# 2024-08-27     Supperthomas the first version
# 2025-08-09     ThearchyHelios     Fix Darwin detection and URL
#

#这个脚本用于安装RT-Thread开发环境 请确保网络畅通

# 设置环境变量 如果希望生效请在当前shell中执行source install.sh

export RTT_ROOT=$(pwd)
export RTT_CC=gcc
RTT_ENV_URL=${RTT_ENV_URL:-https://github.com/CYFS3/env.git}
RTT_ENV_BRANCH=${RTT_ENV_BRANCH:-feat_env}

echo "RTT_ROOT is set to: $RTT_ROOT"

run_env_installer() {
    installer_script=$1
    shift
    installer_dir=${TMPDIR:-/tmp}/cyfs3-env-installer

    rm -rf "$installer_dir"
    git clone --depth 1 --branch "$RTT_ENV_BRANCH" "$RTT_ENV_URL" "$installer_dir"
    chmod +x "$installer_dir/$installer_script"
    "$installer_dir/$installer_script" "$@"
    rm -rf "$installer_dir"
}


check_if_china_ip() {
    # 默认情况下不使用gitee
    use_gitee=false

    # 尝试通过IP地址判断
    ip=$(curl -s https://ifconfig.me/ip)
    if [ -n "$ip" ]; then
        location=$(curl -s http://www.ip-api.com/json/$ip | grep -o '"country":"China"')
        if [ "$location" == '"country":"China"' ]; then
            use_gitee=true
            echo "Detected China IP. Using gitee."
        else
            echo "IP location is not in China."
        fi
    else
        echo "Failed to retrieve IP address. Falling back to timezone check."
        
        # 通过时区判断
        if [ $(($(date +%z)/100)) -eq 8 ]; then
            use_gitee=true
            echo "Detected timezone UTC+8. Using gitee."
        else
            echo "Timezone is not UTC+8."
        fi
    fi

    echo $use_gitee
}


# 检测操作系统类型和发行版
detect_os() {
    if command -v uname >/dev/null 2>&1; then
        OS=$(uname -s)
    else
        if [ -f "/etc/os-release" ]; then
            OS="Linux"
        elif [ -f "/System/Library/CoreServices/SystemVersion.plist" ]; then
            OS="Darwin"
        elif [[ -d "/mnt/c/Windows" || -d "/c/Windows" ]]; then
            OS="WSL"
        else
            OS="UNKNOWN"
        fi
    fi

    if [ "$OS" == "Linux" ]; then
        if [ -f /etc/os-release ]; then
            . /etc/os-release
            DISTRO=$ID
            VERSION=$VERSION_ID
        elif [ -f /etc/lsb-release ]; then
            . /etc/lsb-release
            DISTRO=$DISTRIB_ID
            VERSION=$DISTRIB_RELEASE
        else
            DISTRO="UNKNOWN"
            VERSION="UNKNOWN"
        fi
    fi

    echo "Detected Operating System: $OS, Distribution: $DISTRO, Version: $VERSION"
}

# 修改的安装函数
install_on_ubuntu() {
    echo "Installing on Debian/Ubuntu..."
    use_gitee=$(check_if_china_ip)

    # 根据检测结果决定是否使用--gitee参数
    if [ "$use_gitee" = true ]; then
        echo "Installing on China gitee..."
        run_env_installer install_ubuntu.sh --gitee
    else
        echo "Installing on no China..."
        run_env_installer install_ubuntu.sh
    fi
}


install_on_fedora() {
    echo "Installing on Fedora..."

}

install_on_centos() {
    echo "Installing on CentOS/RHEL..."
}

install_on_arch() {
    echo "Installing on Arch Linux..."
}

install_on_macos() {
    echo "Installing on macOS..."
    use_gitee=$(check_if_china_ip)

    # 根据检测结果决定是否使用--gitee参数
    if [ "$use_gitee" = true ]; then
        echo "Installing on China gitee..."
        run_env_installer install_macos.sh --gitee
    else
        echo "Installing on no China..."
        run_env_installer install_macos.sh
    fi
}

install_on_wsl() {
    echo "Installing on Windows Subsystem for Linux (WSL)..."
}

install_on_windows() {
    echo "Installing on Windows using PowerShell..."
        use_gitee=$(check_if_china_ip)

    # 根据检测结果决定是否使用--gitee参数
    if [ "$use_gitee" = true ]; then
        echo "Installing on China gitee..."
        run_env_installer install_windows.ps1 --gitee
    else
        echo "Installing on no China..."
        run_env_installer install_windows.ps1
    fi
}

install_on_opensuse() {
    echo "Installing on openSUSE..."
    use_gitee=$(check_if_china_ip)
    if [ "$use_gitee" = true ]; then
        echo "Installing on China gitee..."
        run_env_installer install_suse.sh --gitee
    else
        echo "Installing on no China..."
        run_env_installer install_suse.sh
    fi
}
# 主函数
main() {
    detect_os
    case "$OS" in
        Linux)
            case "$DISTRO" in
                ubuntu|debian)
                    install_on_ubuntu
                    ;;
                fedora)
                    install_on_fedora
                    ;;
                centos|rhel)
                    install_on_centos
                    ;;
                arch)
                    install_on_arch
                    ;;
                *)
                    echo "Unsupported Linux distribution: $DISTRO"
                    exit 1
                    ;;
            esac
            ;;
        Darwin)
            install_on_macos
            ;;
        WSL)
            install_on_wsl
            ;;
        Windows)
            install_on_windows
            ;;
        *)
            echo "Unsupported Operating System: $OS"
            exit 1
            ;;
    esac
    echo "Installation completed!"
}

# 执行主函数
main

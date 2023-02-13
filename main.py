import fileinput
import os
import subprocess
import sys

packages = [
    'adobe-source-code-pro-fonts',
    'alacritty',
    'base-devel',
    'bat',
    'brightnessctl'
    'chromium',
    'htop',
    'vim',
]


def check_user():
    if os.geteuid() != 0:
        sys.exit("error: must be run as root")


def install_packages():
    subprocess.run(['pacman', '-S', '--noconfirm', '--needed'] + packages)


# Replaces commented values in default config (will no-op if config is empty)
def configure_pacman():
    with fileinput.input(files='/etc/pacman.conf', inplace=True) as f:
        for line in f:
            match line.strip():
                case '#Color':
                    print('Color')
                case l if l.startswith('#ParallelDownloads'):
                    print('ParallelDownloads = 10')
                case _:
                    print(line, end='')


check_user()
configure_pacman()
install_packages()

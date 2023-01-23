import subprocess

packages = ['htop', 'vim', 'base-devel', 'otf-codenewroman-nerd', 'alacritty', 'bat']


def install():
    subprocess.run(['sudo', 'pacman', '-S', '--needed'] + packages)


install()

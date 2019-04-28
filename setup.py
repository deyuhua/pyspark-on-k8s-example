#! /usr/bin/env python
#
# -*- coding: utf-8 -*-

import os
import shutil
from distutils.command.clean import clean as Clean

__author__ = "HUADEYU"
__maintainer__ = "HUADEYU"
__email__ = "huadeyu@gmail.com"


class CleanCommand(Clean):
    description = "Remove build artifacts from the source tree"

    def run(self):
        Clean.run(self)

        if os.path.exists('build'):
            shutil.rmtree('build')
        for dirpath, dirnames, filenames in os.walk('engine'):
            for filename in filenames:
                if any(filename.endswith(suffix) for suffix in (".so", ".pyd", ".dll", ".pyc")):
                    os.unlink(os.path.join(dirpath, filename))
                    continue
            for dirname in dirnames:
                if dirname == '__pycache__':
                    shutil.rmtree(os.path.join(dirpath, dirname))


cmdclass = {'clean': CleanCommand}


def setup_package():
    try:
        from setuptools import setup, find_packages
    except ImportError:
        from distutils.core import setup, find_packages

    with open('requirements.txt', 'r', encoding='utf-8') as f:
        install_requires = [pkg for pkg in f.read().split("\n") if pkg]

    metadata = dict(
        cmdclass=cmdclass,
        install_requires=install_requires,
        scripts=['src/run.py'],
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()

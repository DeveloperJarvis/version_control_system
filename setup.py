# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Version Control System Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Version Control System - Build a mini Git with commit, diff, branch
# Skills: hashing, file systems, DAGs
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# setup MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from setuptools import setup, find_packages


setup(
    name="vcs",
    version="0.1.0",
    description="Version Control System (Git Implementation)",
    author="Developer Jarvis",
    author_email="developerjarvis@github.com",
    license="GPL-3.0-or-later",
    packages=find_packages(
        exclude=("tests*", "logs*",)
    ),
    python_requires=">=3.9",
    install_requires=[],
    include_package_data=True,
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
            "mypy",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)

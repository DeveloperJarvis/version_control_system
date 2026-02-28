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
# file_utils MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import os
from pathlib import Path


def ensure_dir(path: str | Path) -> None:
    """
    Create directory if it does not exist
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def read_file_bytes(path: str | Path) -> bytes:
    """
    Read file as bytes
    """
    with open(path, "rb") as f:
        return f.read()


def write_file_bytes(path: str | Path, data: bytes) -> None:
    """
    Write bytes to file, creating directories if needed
    """
    path = Path(path)
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "wb") as f:
        f.write(data)


def read_file_text(path: str | Path) -> str:
    """
    Read file as UTF-8 text
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file_text(path: str | Path, data: str) -> None:
    """
    Write text to file
    """
    path = Path(path)
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)


def remove_file(path: str | Path) -> None:
    """
    Remove file if exists
    """
    path = Path(path)
    if path.exists() and path.is_file():
        path.unlink()

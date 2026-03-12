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
# object_store MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from pathlib import Path
from vcs.utils.constants import VCS_DIR, OBJECTS_DIR
from vcs.utils.file_utils import (
    write_file_bytes,
    read_file_bytes,
    ensure_dir,
)


class ObjectStore:
    """
    Content-addressable storage
    """

    def __init__(self, root: Path):
        self.root = root
        self.objects_path = root / VCS_DIR / OBJECTS_DIR

    def _get_object_path(self, obj_hash: str) -> Path:
        subdir = obj_hash[:2]
        filename = obj_hash[2:]
        path = self.objects_path / subdir
        ensure_dir(path)
        return path / filename
    
    def write(self, obj):
        obj_hash = obj.compute_hash()
        path = self._get_object_path(obj_hash)

        if not path.exists():
            write_file_bytes(path, obj.serialize())
        
        return obj_hash
    
    def read(self, obj_hash: str) -> bytes:
        path = self._get_object_path(obj_hash)
        return read_file_bytes(path)
    
    def exists(self, obj_hash: str) -> bool:
        return self._get_object_path(obj_hash).exists()

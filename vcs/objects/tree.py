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
# tree MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from .base import GitObject
from vcs.utils.constants import OBJECT_TYPE_TREE


class Tree(GitObject):
    """
    Represents directory snapshot
    """

    object_type = OBJECT_TYPE_TREE

    def __init__(self):
        self.entries = []   # list of (name, type, hash)
    
    def add_entry(self, name: str, obj_type: str,
                  obj_hash: str):
        self.entries.append((name, obj_type, obj_hash))
    
    def serialize(self):
        """
        Deterministic serialization (sorted)
        """
        sorted_entries = sorted(self.entries,
                                key=lambda x: x[0])
        lines = [
            f"{obj_type} {obj_hash} {name}"
            for name, obj_type, obj_hash in sorted_entries
        ]
        return "\n".join(lines).encode()

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
# commit MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import time
from .base import GitObject
from vcs.utils.constants import OBJECT_TYPE_COMMIT


class Commit(GitObject):
    """
    Represents snapshot commit
    Forms DAG
    """

    object_type = OBJECT_TYPE_COMMIT

    def __init__(
        self,
        tree_hash: str,
        parent_hashes: list[str] | None,
        author: str,
        message: str,
        timestamp: float | None = None,
    ):
        self.tree_hash = tree_hash
        self.parent_hashes = parent_hashes or []
        self.author = author
        self.message = message
        self.timestamp = timestamp or time.time()

    def serialize(self) -> bytes:
        lines = [
            f"tree {self.tree_hash}",
        ]

        for parent in self.parent_hashes:
            lines.append(f"parent {parent}")
        
        lines.append(f"author {self.author}")
        lines.append(f"timestamp {self.timestamp}")
        lines.append("")
        lines.append(self.message)

        return "\n".join(lines).encode()

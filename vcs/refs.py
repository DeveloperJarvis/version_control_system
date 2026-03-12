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
# refs MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from pathlib import Path
from vcs.utils.constants import (
    VCS_DIR,
    REFS_DIR,
    HEADS_DIR,
    HEAD_FILE,
    DEFAULT_BRANCH,
)
from vcs.utils.file_utils import (
    write_file_text,
    read_file_text,
    ensure_dir,
)


class RefManager:
    """
    Manges HEAD and branch references
    """

    def __init__(self, root: Path):
        self.root = root
        self.refs_path = root / VCS_DIR / REFS_DIR / HEADS_DIR
        self.head_file = root / VCS_DIR / HEAD_FILE
        ensure_dir(self.refs_path)
    
    def init(self):
        self.create_branch(DEFAULT_BRANCH, None)
        write_file_text(self.head_file, DEFAULT_BRANCH)
    
    def get_current_branch(self):
        return read_file_text(self.head_file).strip()
    
    def get_head_commit(self):
        branch = self.get_current_branch()
        branch_path = self.refs_path / branch
        if not branch_path.exists():
            return None
        return read_file_text(branch_path).strip()
    
    def update_head(self, commit_hash: str):
        branch = self.get_current_branch()
        write_file_text(self.refs_path / branch, commit_hash)

    def create_branch(self, name: str, commit_hash: str | None):
        write_file_text(self.refs_path / name, commit_hash or "")
    
    def checkout(self, name: str):
        if not (self.refs_path / name).exists():
            raise ValueError(
                f"Branch '{name}' does not exist"
            )
        write_file_text(self.head_file, name)

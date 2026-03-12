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
# index MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import json
from pathlib import Path
from vcs.utils.constants import VCS_DIR, INDEX_FILE
from vcs.utils.file_utils import write_file_text, read_file_text


class Index:
    """
    Staging area
    Tracks: file_path -> blob_hash
    """

    def __init__(self, root: Path):
        self.root = root
        self.index_path = root / VCS_DIR / INDEX_FILE
        self.entries = self._load()

    def _load(self):
        if not self.index_path.exists():
            return {}
        return json.loads(read_file_text(self.index_path))
    
    def add(self, file_path: str, blob_hash: str):
        self.entries[file_path] = blob_hash
        self._save()
    
    def clear(self):
        self.entries = {}
        self._save()

    def _save(self):
        write_file_text(self.index_path,
                        json.dumps(self.entries, indent=2))

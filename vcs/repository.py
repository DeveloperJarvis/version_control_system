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
# repository MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from pathlib import Path
from vcs.utils.constants import VCS_DIR
from vcs.utils.file_utils import ensure_dir, read_file_bytes
from vcs.objects import Blob, Tree, Commit
from vcs.index import Index
from vcs.object_store import ObjectStore
from vcs.refs import RefManager


class Repository:
    """
    High-level orchestrator
    """

    def __init__(self, root: str | Path = "."):
        self.root = Path(root)
        self.vcs_dir = self.root / VCS_DIR

        self.object_store = ObjectStore(self.root)
        self.index = Index(self.root)
        self.refs = RefManager(self.root)
        ensure_dir(self.vcs_dir / "objects")
    
    def init(self):
        ensure_dir(self.vcs_dir)
        self.refs.init()
    
    def add(self, file_path: str):
        content = read_file_bytes(self.root / file_path)
        blob = Blob(content)
        blob_hash = self.object_store.write(blob)
        self.index.add(file_path, blob_hash)
    
    def commit(self, message: str, author: str = "Developer"):
        tree = Tree()

        for file_path, blob_hash in self.index.entries.items():
            tree.add_entry(file_path, "blob", blob_hash)
        
        tree_hash = self.object_store.write(tree)

        parent = self.refs.get_head_commit()
        parents = [parent] if parent else []

        commit = Commit(
            tree_hash=tree_hash,
            parent_hashes=parents,
            author=author,
            message=message,
        )

        commit_hash = self.object_store.write(commit)
        self.refs.update_head(commit_hash)
        self.index.clear()

        return commit_hash
    
    def log(self):
        current = self.refs.get_head_commit()

        while current:
            data = self.object_store.read(current).decode()
            print(f"\ncommit {current}")
            print(data)

            parent_line = next(
                (line for line in data.splitlines()
                 if line.startswith("parent ")),
                 None,
            )

            if parent_line:
                current = parent_line.split()[1]
            else:
                break

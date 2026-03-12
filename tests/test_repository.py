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
# test_repository MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import tempfile
from pathlib import Path

from vcs.repository import Repository


def test_init_creates_repo():
    with tempfile.TemporaryDirectory() as tmp:
        repo = Repository(tmp)
        repo.init()

        assert (Path(tmp) / ".vcs").exists()


def test_add_and_commit():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        file_path = root / "test.txt"
        file_path.write_text("hello")

        repo = Repository(tmp)
        repo.init()
        repo.add("test.txt")
        commmit_hash = repo.commit("Test commit")

        assert commmit_hash is not None
        assert repo.refs.get_head_commit() == commmit_hash

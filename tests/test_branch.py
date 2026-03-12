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
# test_branch MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import tempfile
from pathlib import Path

from vcs.repository import Repository


def test_branch_creation():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        file_path = root / "a.txt"
        file_path.write_text("data")

        repo = Repository(tmp)
        repo.init()
        repo.add("a.txt")
        commit_hash = repo.commit("Initial")

        repo.refs.create_branch("feature", commit_hash)

        branch_path = root / ".vcs" / "refs" / "heads" / "feature"
        assert branch_path.exists()
        assert branch_path.read_text().strip() == commit_hash

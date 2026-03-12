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
# test_commit MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import tempfile
from pathlib import Path

from vcs.objects import Commit


def test_commit_hash_stability():
    commit1 = Commit(
        tree_hash="abc123",
        parent_hashes=[],
        author="Tester",
        message="Initial commit",
        timestamp=123456,
    )

    commit2 = Commit(
        tree_hash="abc123",
        parent_hashes=[],
        author="Tester",
        message="Initial commit",
        timestamp=123456,
    )

    assert commit1.compute_hash() == commit2.compute_hash()


def test_commit_multiple_parents():
    commit = Commit(
        tree_hash="treehash",
        parent_hashes=["p1", "p2"],
        author="Tester",
        message="Merge commit",
        timestamp=123,
    )

    serialized = commit.serialize().decode()
    assert "parent p1" in serialized
    assert "parent p2" in serialized

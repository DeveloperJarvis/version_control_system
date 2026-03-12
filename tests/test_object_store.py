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
# test_object_store MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import tempfile
from pathlib import Path

from vcs.object_store import ObjectStore
from vcs.objects import Blob

def test_write_and_read_objects():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = ObjectStore(root)

        blob = Blob(b"hello world")
        obj_hash = store.write(blob)

        assert store.exists(obj_hash)

        data = store.read(obj_hash)
        assert data == b"hello world"


def test_object_deduplication():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = ObjectStore(root)

        blob1 = Blob(b"same")
        blob2 = Blob(b"same")

        hash1 = store.write(blob1)
        hash2 = store.write(blob2)

        assert hash1 == hash2

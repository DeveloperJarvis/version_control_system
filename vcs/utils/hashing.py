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
# hashing MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import hashlib
from .constants import HASH_ALGORITHM


def compute_hash(data: bytes) -> str:
    """
    Compute cryptographic hash of given bytes

    Uses algorithm defined in constants
    """
    if HASH_ALGORITHM == "sha1":
        hasher = hashlib.sha1()
    elif HASH_ALGORITHM == "sha256":
        hasher = hashlib.sha256()
    else:
        raise ValueError(
            f"Unsupported hash algorithm: {HASH_ALGORITHM}"
        )

    hasher.update(data)
    return hasher.hexdigest()


def compute_object_hash(object_type: str,
                        content: bytes) -> str:
    """
    Compute Git-style object hash:
    hash("<type> <size>\\0<content>")
    """
    header = f"{object_type} {len(content)}\0".encode()
    full_data = header + content
    return compute_hash(full_data)

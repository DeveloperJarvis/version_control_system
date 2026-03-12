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
# base MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from abc import ABC, abstractmethod
from vcs.utils.hashing import compute_object_hash


class GitObject(ABC):
    """
    Abstract base class for all VCS objects
    """

    object_type: str

    @abstractmethod
    def serialize(self) -> bytes:
        """
        Convert object into storable bytes
        """
        pass

    def compute_hash(self) -> str:
        """
        Compute content-addressable hash
        """
        return compute_object_hash(self.object_type,
                                   self.serialize())

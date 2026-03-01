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
# diff_engine MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from .lcs import lcs_matrix, backtrack_lcs


# --------------------------------------------------
# diff engine
# --------------------------------------------------
class DiffEngine:
    """
    High-level diff engine using LCS
    """
    
    @staticmethod
    def diff_text(old: str, new: str) -> str:
        """
        Line-based diff between two text blobs
        """
        old_lines = old.splitlines()
        new_lines = new.splitlines()

        dp = lcs_matrix(old_lines, new_lines)
        lcs = backtrack_lcs(dp, old_lines, new_lines)

        result = []
        i = j = 0

        for line in lcs:
            while old_lines[i] != line:
                result.append(f"- {old_lines[i]}")
                i += 1
            while new_lines[j] != line:
                result.append(f"- {new_lines[j]}")
                j += 1
            
            result.append(f"  {line}")
            i += 1
            j += 1
        
        while i < len(old_lines):
            result.append(f"- {old_lines[i]}")
            i += 1
        while j < len(new_lines):
            result.append(f"- {new_lines[j]}")
            j += 1

        return "\n".join(result)

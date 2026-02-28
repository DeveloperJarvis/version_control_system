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
# config MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import os
from pathlib import Path


# --------------------------------------------------
# app config
# --------------------------------------------------
class AppConfig:
    """
    Application configuration loader
    """

    def __init__(self):
        self.app_name = "VCS"
        self.version = "0.1.0"

        # Logging defaults
        self.log_level = os.getenv("VCS_LOG_LEVEL", "INFO")
        self.log_to_file = True
        self.log_file_path = os.getenv(
            "VCS_LOG_FILE",
            str(Path("logs") / "vcs.log")
        )

        self._ensure_log_directory()
    
    def _ensure_log_directory(self):
        """
        Ensure log directory exists
        """
        log_path = Path(self.log_file_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)

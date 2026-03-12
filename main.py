# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the [Project Name] Library. This library is free
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
# [Project Name] - [brief description of what it does]
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# main MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import sys
import argparse
import logging

from config.config import AppConfig
from vcs.repository import Repository
from vcs.commands.init import InitCommand
from vcs.commands.add import AddCommand
from vcs.commands.commit import CommitCommand
from vcs.commands.log import LogCommand
from vcs.commands.branch import BranchCommand
from vcs.commands.checkout import CheckoutCommand
from vcs.commands.diff import DiffCommand


def setup_logging(config: AppConfig):
    log_level = getattr(logging, config.log_level.upper(),
                        logging.INFO)
    
    logging.basicConfig(
        level=log_level,
        filename=(config.log_file_path
        if config.log_to_file else None),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

def build_parser():
    parser = argparse.ArgumentParser(prog="vcs")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("files", nargs="+")

    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("-m", "--message",
                               required=True)
    
    subparsers.add_parser("log")

    branch_parser = subparsers.add_parser("branch")
    branch_parser.add_argument("name")

    checkout_parser = subparsers.add_parser("checkout")
    checkout_parser.add_argument("name")

    subparsers.add_parser("diff")

    return parser


def main():
    config = AppConfig()
    setup_logging(config)

    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    repo = Repository()

    if args.command == "init":
        InitCommand(repo).execute()
    
    elif args.command == "add":
        AddCommand(repo).execute(args.files)
    
    elif args.command == "commit":
        CommitCommand(repo).execute(args.message)
    
    elif args.command == "log":
        LogCommand(repo).execute()
    
    elif args.command == "branch":
        BranchCommand(repo).execute(args.name)
    
    elif args.command == "checkout":
        CheckoutCommand(repo).execute(args.name)
    
    elif args.command == "diff":
        DiffCommand(repo).execute()
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

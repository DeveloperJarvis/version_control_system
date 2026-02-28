@echo off

REM Root directory
@REM set ROOT=log_pattern_detection_tool
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\vcs"
call :create_folder "%ROOT%\vcs\commands"
call :create_folder "%ROOT%\vcs\diff"
call :create_folder "%ROOT%\vcs\objects"
call :create_folder "%ROOT%\vcs\utils"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"
call :create_py_file "%ROOT%\setup.py"

call :create_py_file "%ROOT%\config\__init__.py"
call :create_py_file "%ROOT%\config\config.py"

call :create_py_file "%ROOT%\vcs\__init__.py"
call :create_py_file "%ROOT%\vcs\index.py"
call :create_py_file "%ROOT%\vcs\object_store.py"
call :create_py_file "%ROOT%\vcs\refs.py"
call :create_py_file "%ROOT%\vcs\repository.py"
call :create_py_file "%ROOT%\vcs\commands\__init__.py"
call :create_py_file "%ROOT%\vcs\commands\add.py"
call :create_py_file "%ROOT%\vcs\commands\branch.py"
call :create_py_file "%ROOT%\vcs\commands\checkout.py"
call :create_py_file "%ROOT%\vcs\commands\commit.py"
call :create_py_file "%ROOT%\vcs\commands\diff.py"
call :create_py_file "%ROOT%\vcs\commands\init.py"
call :create_py_file "%ROOT%\vcs\commands\log.py"
call :create_py_file "%ROOT%\vcs\diff\__init__.py"
call :create_py_file "%ROOT%\vcs\diff\diff_engine.py"
call :create_py_file "%ROOT%\vcs\diff\lcs.py"
call :create_py_file "%ROOT%\vcs\objects\__init__.py"
call :create_py_file "%ROOT%\vcs\objects\base.py"
call :create_py_file "%ROOT%\vcs\objects\blob.py"
call :create_py_file "%ROOT%\vcs\objects\commit.py"
call :create_py_file "%ROOT%\vcs\objects\tree.py"
call :create_py_file "%ROOT%\vcs\utils\__init__.py"
call :create_py_file "%ROOT%\vcs\utils\constants.py"
call :create_py_file "%ROOT%\vcs\utils\file_utils.py"
call :create_py_file "%ROOT%\vcs\utils\hashing.py"

call :create_py_file "%ROOT%\tests\__init__.py"
call :create_py_file "%ROOT%\tests\test_branch.py"
call :create_py_file "%ROOT%\tests\test_commit.py"
call :create_py_file "%ROOT%\tests\test_diff.py"
call :create_py_file "%ROOT%\tests\test_object_store.py"
call :create_py_file "%ROOT%\tests\test_repository.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\logs\vcs.log"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"
call :create_file "%ROOT%\.env"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Version Control System Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Version Control System - Build a mini Git with commit, diff, branch
echo # Skills: hashing, file systems, DAGs
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b
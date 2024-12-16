#!/usr/bin/env python

# Import built-in libraries
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

# Import 3rd-party libraries
from aocd.models import Puzzle
from rich.console import Console
from rich.prompt import Confirm

# Globals
PROJECT_ROOT = Path(os.getcwd())


def cmd_is_installed(cmd: str) -> bool:
    return False if shutil.which(cmd) is None else True


def init_local_git_repo() -> None:
    _name = "{{ cookiecutter.project_slug }}"
    subprocess.run(["git", "init"], check=True)


def create_github_repo(console: Console) -> None:
    _success = False
    _name = "{{ cookiecutter.project_slug }}"
    _description = "{{ cookiecutter.project_description }}"
    _command = ["gh", "repo", "create", _name, "--public", "--description", _description, "--source", os.getcwd()]
    with console.status("[bold green]Creating repository...[/bold green]", spinner="dots"):
        try:
            process = subprocess.run(_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if process.returncode == 0:
                console.print(f"[bold green]Repository \"{_name}\" created successfully![/bold green]")
                _success = True
            else:
                console.print(f"[bold red]Failed to create repository: {process.stderr.strip()}[/bold red]")
                _success = False
        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred: {str(e)}[/bold red]")


def populate_data() -> None:
    _year, _day = re.search(r".+?-(\d{4}).+\.(\d{2})", "{{ cookiecutter.project_slug }}").groups()
    print(f"DEBUG: _year = {_year}, _day = {_day}")
    _puzzle = Puzzle(year=int(_year), day=int(_day))
    data = _puzzle.input_data.splitlines()
    data_file = PROJECT_ROOT.joinpath("data", "data.txt")
    data_file.write_text("\n".join(data))


def push_initial_commit() -> None:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit 🎉"], check=True)
    subprocess.run(["git", "push", "--set-upstream", "origin", "main"], check=True)


def main() -> None:
    _msg = "gh command is not installed. Please install it and try again."
    if not cmd_is_installed("gh"):
        print(_msg)
        sys.exit(0)

    console = Console()

    populate_data()
    init_local_git_repo()

    if not Confirm.ask("Do you want to create a new GitHub repository?"):
        console.print("[red]GitHub repository will not be created.[/red]")
        sys.exit(0)

    create_github_repo(console)
    push_initial_commit()


if __name__ == "__main__":
    main()

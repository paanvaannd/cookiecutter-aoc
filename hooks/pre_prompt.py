#!/usr/bin/env python

# Import built-in libraries
from datetime import datetime
import json
import os
from pathlib import Path

# Import 3rd-party libraries
from aocd.models import Puzzle
from rich.prompt import Confirm, IntPrompt

# Globals
SCRIPT_PATH = Path(os.path.abspath(__file__))
SCRIPT_ROOT = SCRIPT_PATH.parent
PROJECT_ROOT = SCRIPT_ROOT.parent


def main() -> None:
    _year = datetime.now().year
    _day= datetime.now().day
    _confirmed: bool = False
    while not _confirmed:
        _confirmed = bool(Confirm(f"Target puzzle year = {_year}, day = {_day}: is this correct?"))
        _year = IntPrompt.ask("What is the year of the target puzzle to solve?")
        _day = IntPrompt.ask("What is the day of the target puzzle?")

    puzzle = Puzzle(year=_year, day=_day)
    config_file = PROJECT_ROOT.joinpath("cookiecutter.json")
    config = json.loads(config_file.read_text())
    config["project_slug"] = f"aoc-{_year}.12.{_day:02d}",
    config["script_name"] = puzzle.title.lower().replace(" ", "_"),
    config["project_description"] = f"Advent of Code {_year}, Day {_day}"
    config_file.write_text(json.dumps(config, indent=4))


if __name__ == "__main__":
    main()

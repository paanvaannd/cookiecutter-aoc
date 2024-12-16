#!/usr/bin/env python

# Import built-in modules
import os
from pathlib import Path

# Globals
SCRIPT_PATH = Path(os.path.abspath(__file__))
SCRIPT_ROOT = SCRIPT_PATH.parent
PROJECT_ROOT = SCRIPT_ROOT.parent


def read_data_file(filename: str) -> str:
    _data_file = PROJECT_ROOT.joinpath("data", filename)
    with open(_data_file, mode="r") as _file:
        return _file.read()


def main() -> None:
    pass


if __name__ == "__main__":
    main()

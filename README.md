# Advent of Code Cookiecutter Template

Status: **WIP**: This documentation, and indeed the project overall, are works-in-progress and as such as liable to change at any time.

_Description_: A strongly-opinionated [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for automating the creation of Advent of Code repositories.

## Requirements

1. Install [`advent-of-code-data` (`aocd`)](https://github.com/wimglenn/advent-of-code-data) to the Python environment from which you run `cookiecutter`.
2. [Configure `aocd`](https://github.com/wimglenn/advent-of-code-data#quickstart) with your unique Advent of Code session ID(s).
3. If you want to be able to automatically create a GitHub repository for your code and link it with the local directory created by `cookiecutter` via this template, please set up [GitHub CLI (`gh`)](https://github.com/cli/cli).

## Usage

After ensuring that all [requirements](#requirements) are met, `cd` into the directory you want to create the project in and run the following command from within the Python environment in which you have set up `cookiecutter`:

```bash
$ cookiecutter gh:paanvaannd/cookiecutter-aoc
```

First, you'll enter when prompted the year (as an integer) and the day (as an integer) for the Advent of Code puzzle you wish to work on.

After doing so, you'll be asked to specify a "project slug." This will be the name of the local repository that is created and also, should you choose to have the script create one, the name of the automatically-created GitHub repository. The default (**recommended**) value is generated based off of the year and day you specified earlier (e.g., `aoc-2024.12.01`).

Next, you'll enter the script name. This will be the name of the package that is set up in the `cookiecutter`-created project. The default name is decided based on the title of the specified puzzle as fetched by `aocd`.

Enter a description for the project. This is only important if you choose to have the script create a GitHub repository for you as well. Your response here will be the description of the created GitHub repository.

The templated directory will be created on your file system and be initialized as a local Git repository. The script then fetches the data from that day's challenge and download it to `data/data.txt`, which is already configured to be loaded within the templated main script (provided the same name as the package, or whatever you entered as the script name).

Finally, if you answer affirmatively, the script will create a GitHub repository of the same name as the project directory that is created by the script (i.e., whatever you entered for the "project slug") and an initial commit will be pushed from the local repository to its new remote on GitHub.

The script automatically includes GitHub Actions to test your code and an appropriately-placed `test` directory within the created project in which you can place your tests. This is strongly encouraged for best practice but is not necessary.

Happy coding! 🧑🏾‍💻

—— Pavan Anand

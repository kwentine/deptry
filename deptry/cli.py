import logging
import pathlib
import sys
from typing import List

import click

from deptry.config import Config
from deptry.core import Core
from deptry.utils import run_within_dir


@click.group()
def deptry() -> None:
    pass


@click.command()
@click.argument("directory", type=click.Path(exists=True))
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Boolean flag for verbosity. Using this flag will display more information about files, imports and dependencies while running.",
)
@click.option(
    "--ignore-dependencies",
    "-i",
    multiple=True,
    help="Dependencies listed in pyproject.toml that should be ignored, even if they are not imported.",
)
@click.option(
    "--ignore-directories",
    "-id",
    multiple=True,
    help="""Directories in which .py files should not be scanned for imports to determine if a dependency is used or not.
    Defaults to 'venv'. Specify multiple directories by using this flag twice, e.g. `-id .venv -id other_dir`""",
)
@click.option(
    "--ignore-notebooks",
    "-nb",
    is_flag=True,
    help="Boolean flag to specify if notebooks should be ignored while scanning for imports.",
)
def check(
    directory: pathlib.Path,
    verbose: bool,
    ignore_dependencies: List[str],
    ignore_directories: List[str],
    ignore_notebooks: bool,
) -> None:

    with run_within_dir(directory):
        log_level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(level=log_level, handlers=[logging.StreamHandler()], format="%(message)s")

        # a dictionary with the cli arguments, if they are used.
        cli_arguments = {}  # type: ignore
        if len(ignore_dependencies) > 0:
            cli_arguments["ignore_dependencies"] = list(ignore_dependencies)
        if len(ignore_directories) > 0:
            cli_arguments["ignore_directories"] = list(ignore_directories)
        if ignore_notebooks:
            cli_arguments["ignore_notebooks"] = True
        config = Config(cli_arguments)

        obsolete_dependencies = Core(
            ignore_dependencies=config.config["ignore_dependencies"],
            ignore_directories=config.config["ignore_directories"],
            ignore_notebooks=config.config["ignore_notebooks"],
        ).run()
        if len(obsolete_dependencies):
            logging.info(f"pyproject.toml contains obsolete dependencies: {obsolete_dependencies}")
            sys.exit(1)
        else:
            logging.info("Succes! No obsolete dependencies found.")
            sys.exit(0)


deptry.add_command(check)

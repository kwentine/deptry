<p align="center">
  <img width="460" height="300" src="static/deptry_Logo-01.svg">
</p>
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
</style>

---

[![Release](https://img.shields.io/github/v/release/fpgmaas/deptry)](https://img.shields.io/github/v/release/fpgmaas/deptry)
[![Build status](https://img.shields.io/github/workflow/status/fpgmaas/deptry/Main/main)](https://github.com/fpgmaas/deptry/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/deptry)](https://pypi.org/project/deptry/)
[![codecov](https://codecov.io/gh/fpgmaas/deptry/branch/main/graph/badge.svg)](https://codecov.io/gh/fpgmaas/deptry)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/deptry)](https://pypistats.org/packages/deptry)
[![License](https://img.shields.io/github/license/fpgmaas/deptry)](https://img.shields.io/github/license/fpgmaas/deptry)

_deptry_ is a command line tool to check for issues with dependencies in a Python project, such as obsolete or missing dependencies. It supports the following types of projects:

- Projects that use [Poetry](https://python-poetry.org/) and a corresponding `pyproject.toml` file
- Projects that use [PDM](https://pdm.fming.dev/latest/) and a corresponding `pyproject.toml` file
- Projects that use any package manager that strictly follows [PEP 621](https://peps.python.org/pep-0621/) dependency specification
- Projects that use a `requirements.txt` file according to the [pip](https://pip.pypa.io/en/stable/user_guide/) standards

Dependency issues are detected by scanning for imported modules within all Python files in a directory and its subdirectories, and comparing those to the dependencies listed in the project's requirements.

---

## Quickstart

### Installation

_deptry_ can be added to your project with

```sh
poetry add --group dev deptry
```

or with

```sh
pip install deptry
```

!!! important

    When using pip to install _deptry_, make sure you install it within the virtual environment of your project. Installing _deptry_ globally will not work, since it needs to have access to the metadata of the packages in the virtual environment.

### Prerequisites

_deptry_ should be run within the root directory of the project to be scanned, and the project should be running in its own dedicated virtual environment.

### Usage

To scan your project for dependency issues, run

```sh
deptry .
```

_deptry_ can be configured by using additional command line arguments, or
by adding a `[tool.deptry]` section in `pyproject.toml`. For more information, see [Usage and Configuration](./usage.md)

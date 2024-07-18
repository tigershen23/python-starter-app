# Python boilerplate

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [What's in the box ?](#whats-in-the-box-)
- [Testing](#testing)
- [Docker](#docker)

---

## Prerequisites

- [Python](https://www.python.org/downloads/) **>=3.12 <3.13** (_tested with 3.12.3_)
- [Pyenv](https://github.com/pyenv/pyenv)
- [pre-commit](https://pre-commit.com/#install)
- [docker](https://docs.docker.com/get-docker/) (_optional_)

---

## Installation

1. Clone the git repository

   ```bash
   git clone https://github.com/tigershen23/python-starter-app.git <myapplication>
   ```

2. Go into the project directory

   ```bash
   cd <myapplication>
   ```

3. Set up the development environment

   ```bash
   pyenv virtualenv 3.12 <app name>
   pyenv activate <app name>
   make dev_install
   ```

4. Do a global search for "myapplication" and rename everything to your app name

5. Rename the directories and files containing "myapplication" to your app name

6. Run `make run` to run the application

---

## What's in the box ?

### Poetry

[Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python. It allows you to
declare the libraries your project depends on and it will manage (install/update) them for you.

**pyproject.toml file** ([`pyproject.toml`](pyproject.toml)): orchestrate your project and its dependencies
**poetry.lock file** ([`poetry.lock`](poetry.lock)): ensure that the package versions are consistent for everyone
working on your project

For more configuration options and details, see the [configuration docs](https://python-poetry.org/docs/).

### pre-commit

[pre-commit](https://pre-commit.com/) is a framework for managing and maintaining multi-language pre-commit hooks.

**.pre-commit-config.yaml file** ([`.pre-commit-config.yaml`](.pre-commit-config.yaml)): describes what repositories and
hooks are installed

For more configuration options and details, see the [configuration docs](https://pre-commit.com/).

### ruff

[ruff](https://github.com/charliermarsh/ruff) is an extremely fast Python linter, written in Rust.

Rules are defined in the [`pyproject.toml`](pyproject.toml).

For more configuration options and details, see the [configuration docs](https://github.com/charliermarsh/ruff#configuration).

### bandit

[bandit](https://bandit.readthedocs.io/) is a tool designed to find common security issues in Python code.

Rules are defined in the [`pyproject.toml`](pyproject.toml).

For more configuration options and details, see the [configuration docs](https://bandit.readthedocs.io/).

### Pydantic

[Pydantic](https://docs.pydantic.dev/) is a data validation and settings management library using Python type annotations. It's used in this project for managing configuration settings.

**settings.py file** ([`src/myapplication/settings.py`](src/myapplication/settings.py)): defines the application settings using Pydantic's `BaseSettings` class.
**.env file** ([`.env`](.env)): contains environment-specific settings that are loaded by Pydantic.
**.env.sample file** ([`.env.sample`](.env.sample)): a template for the .env file, showing which environment variables are used by the application.

For more configuration options and details, see the [Pydantic documentation](https://docs.pydantic.dev/).

### pyright

[pyright](https://github.com/microsoft/pyright) is a fast type checker meant for large Python source bases. It can run in a "watch" mode and performs fast incremental updates when files are modified.

Configuration for pyright is defined in the [`pyproject.toml`](pyproject.toml) file.

For more configuration options and details, see the [configuration docs](https://github.com/microsoft/pyright#configuration).

### Typer CLI

[Typer](https://typer.tiangolo.com/) is a library for building CLI applications that users will love using and developers will love creating. It's based on Python 3.6+ type hints.

**cli.py file** ([`src/myapplication/cli.py`](src/myapplication/cli.py)): defines the CLI application using Typer.

The CLI can be invoked using the `myapplication` command after installation. For example:

```bash
myapplication --help
myapplication tiger
```

For more configuration options and details, see the [Typer documentation](https://typer.tiangolo.com/).

### Modal Serverless App

[Modal](https://modal.com/) is a platform for building and deploying serverless applications. This project includes a simple Modal app that demonstrates how to run Python functions in the cloud.

**modal_app.py file** ([`modal_app.py`](modal_app.py)): defines a Modal application with a simple square function and a local entrypoint.

The Modal app can be run using the following command:

```bash
modal run modal_app.py
```

This will execute the local entrypoint function, which in turn calls the remote square function and prints the result.

For more configuration options and details, see the [Modal documentation](https://modal.com/docs).

### Streamlit App

[Streamlit](https://streamlit.io/) is an open-source app framework for Machine Learning and Data Science teams. This project includes a simple Streamlit app that demonstrates how to create interactive web applications with Python.

**streamlit_app.py file** (`streamlit_app.py`): defines a Streamlit application that imports and runs the main function from the `myapplication` package, displaying its output in a web interface.

The Streamlit app can be run using the following command:

```bash
streamlit run streamlit_app.py
```

This will start a local Streamlit server and open the app in your default web browser. The app displays the output of the main function from myapplication as a large heading (h1) element.

For more configuration options and details, see the [Streamlit documentation](https://docs.streamlit.io/).

---

## Testing

We are using [pytest](https://docs.pytest.org/) & [pytest-cov](https://github.com/pytest-dev/pytest-cov) to write tests.

To run tests:

```bash
poetry run pytest tests
```

<details>

<summary>Output</summary>

```text
collected 1 item

tests/test_myapplication.py::test_hello_world PASSED
```

</details>

To run tests with coverage:

```bash
poetry run pytest tests --cov=src
```

<details>

<summary>Output</summary>

```text
collected 1 item

tests/test_myapplication.py::test_hello_world PASSED

---------- coverage: platform linux, python 3.10.4-final-0 -----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
src/myapplication/__init__.py       1      0   100%
src/myapplication/main.py           6      2    67%
---------------------------------------------------
TOTAL                               7      2    71%
```

</details>

---

## Docker

### Build

To build the docker `production` image using [`Dockerfile`](Dockerfile):

```bash
docker build . -t my-python-application:latest
```

To build the docker `development` image using [`Dockerfile`](Dockerfile):

```bash
docker build . --target development -t my-python-application:dev
```

### Run

To run the python app example inside Docker:

```bash
docker run -it --rm my-python-application:latest # or :dev for development
```

<details>

<summary>Output</summary>

```text
Hello World
```

</details>

### Execute command inside container

```bash
docker run -it --rm my-python-application:latest bash
```

---

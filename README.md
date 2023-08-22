# Japanese LLM Chatbot
[![version](https://img.shields.io/badge/version-v0.1.0-green)](https://github.com/ayk24/japanese-llm-chatbot/blob/main/pyproject.toml)
[![Python version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![black](https://img.shields.io/badge/code%20style-black-333333.svg)](https://github.com/psf/black)

## Overview
Build Japanese LLM Chatbot with streamlit

## Setup
### Installing Poetry
This package requires [poetry](https://python-poetry.org/docs/).
- Linux / macOS / Windows (WSL) install instructions
    ```bash
    $ curl -sSL https://install.python-poetry.org | python3 -
    ```
- Windows (Powershell) install instructions
    ```bash
    $ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

### Installing Dependencies
```bash
$ cd japanese-llm-chatbot
$ poetry install
```

## Refactoring
This package uses multiple python linters(`isort`, `black`).
```bash
$ make lint
```
or
```python
$ poetry run isort .
$ poetry run black .
```

## Usage
```bash
$ make run
```

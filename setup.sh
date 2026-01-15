#!/bin/bash

# Example launch:
# bash setup.sh

# -----------------------------------------------------------------------------
# Python venv setup with uv

# install uv (if not already installed)
command -v uv &> /dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh

# create a .venv local virtual environment (if it doesn't exist)
[ -d ".venv" ] || uv venv

# install the repo dependencies
uv sync

# activate venv so that `python` uses the project's venv instead of system python
source .venv/bin/activate

# Python Development Environments

## conda

- conda is a package and environment management system provided by Anaconda.
- You can create a conda environment using the command `conda create --name <env_name> python=3.9`.
- Activate the conda environment using the command `conda activate <env_name>`.
- update conda: `conda activate base && conda update conda`
`conda update -n base -c defaults conda`
- example: create, activate, delete, list, etc: 
`conda create --name myenv python=3.6`
`conda activate myenv`
`conda deactivate`
`conda remove --name myenv --all`
`conda env list`
- 
## pyenv

- pyenv is a tool that allows you to manage **multiple Python versions** on your system.
- Pyenv **does not officially support Windows** and does not work in Windows outside the Windows Subsystem for Linux.
- It allows you to switch between different Python versions easily.
- check https://github.com/pyenv-win/pyenv-win
- You can install different Python versions using the command `pyenv install <version>`.
- Set a global Python version using the command `pyenv global <version>`.

## poetry

- poetry is a dependency management and packaging tool for Python.
- It allows you to manage dependencies and create virtual environments.
- You can create a poetry environment using the command `poetry install`.
- Activate the poetry environment using the command `poetry shell`.

## venv

- venv is a built-in module in Python that allows you to create isolated Python environments.
- It is lightweight and easy to use.
- You can create a virtual environment using the command `python -m venv <path_to_env>`.
- Activate the virtual environment using the command `<path_to_env>/scripts/activate.bat`.

## pipenv

- pipenv is a tool that combines package management with virtual environments.
- It automatically creates and manages a Pipfile to track dependencies and a Pipfile.lock to ensure deterministic
  builds.
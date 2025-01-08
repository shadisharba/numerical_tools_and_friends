conda env export --no-builds> python_env_conda.yml && pip freeze > python_env_pip.txt

@REM conda create --name genAI python==3.12
@REM conda activate genAI
@REM pip install -r python_env_pip.txt
@REM conda env create -f python_env_conda.yml
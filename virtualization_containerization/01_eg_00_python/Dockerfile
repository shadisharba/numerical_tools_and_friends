ARG UV_VER=latest
ARG DEBIAN_VER=latest

FROM ghcr.io/astral-sh/uv:$UV_VER AS uv
FROM mcr.microsoft.com/vscode/devcontainers/base:$DEBIAN_VER
COPY --from=uv --chown=vscode: /uv /uvx /bin/

SHELL ["/bin/bash", "-c"]
USER vscode

ARG DEBIAN_FRONTEND=noninteractive
ARG PYTHON_VER=3.13
ARG VIRTUAL_ENV="/home/vscode/.venv"
ARG WORKING_DIR="/workspaces/01_eg_00_python/"

ENV VIRTUAL_ENV=$VIRTUAL_ENV
ENV WORKING_DIR=$WORKING_DIR
ENV activate="source $VIRTUAL_ENV/bin/activate"
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=True
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

RUN sudo apt update -qq && sudo apt install -qq -y x11-apps
RUN uv python install $PYTHON_VER
RUN uv venv $VIRTUAL_ENV

COPY requirements.txt /
RUN $activate && uv pip install -r requirements.txt
WORKDIR $WORKING_DIR

ENTRYPOINT ["/bin/bash"]
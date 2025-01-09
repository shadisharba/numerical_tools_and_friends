ARG UV_VER=0.5.5
ARG DEBIAN_VER=bookworm

FROM ghcr.io/astral-sh/uv:$UV_VER AS uv
FROM mcr.microsoft.com/vscode/devcontainers/base:$DEBIAN_VER

RUN sudo apt update -qq && sudo apt install -qq -y x11-apps
SHELL ["/bin/bash", "-c"]
USER vscode

ARG DEBIAN_FRONTEND=noninteractive
ARG PYTHON_VER=3.13
ARG UV_VENV="/home/vscode/.venv"
ARG WORKING_DIR="/workspaces/myproject/"

ENV UV_VENV=$UV_VENV
ENV WORKING_DIR=$WORKING_DIR

ENV PYTHONUNBUFFERED=True

COPY --from=uv --chown=vscode: /uv /uvx /bin/
RUN uv python install $PYTHON_VER
RUN echo 'alias activate="source $UV_VENV/bin/activate"' >> ~/.bashrc

COPY init_python.sh $WORKING_DIR
WORKDIR $WORKING_DIR

ENTRYPOINT ["./init_python.sh"]
# ENTRYPOINT ["/bin/bash"]

#!/usr/bin/env bash

uv venv $UV_VENV && source $UV_VENV/bin/activate

/bin/bash

# exec "$@" is typically used to make the entrypoint a pass through that then runs the command passed to the container.
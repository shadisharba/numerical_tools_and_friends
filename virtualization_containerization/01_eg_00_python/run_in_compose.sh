#!/usr/bin/env bash

# xhost +local:root # allow root to access the display & not needed if you run as a standard user
docker compose up --build -d --remove-orphans && docker compose run 01_eg_00_python && docker compose down
# xhost -local:root
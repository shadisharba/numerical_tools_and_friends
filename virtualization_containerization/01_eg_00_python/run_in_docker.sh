#!/usr/bin/env bash

IMAGER_NAME=myimage
docker build -t $IMAGER_NAME --progress plain . && docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -it $IMAGER_NAME /bin/bash
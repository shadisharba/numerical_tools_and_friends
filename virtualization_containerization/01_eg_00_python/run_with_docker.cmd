@echo off
docker build -t dev_image .
docker rm -f dev_container 2>nul
docker run --name dev_container -i -t dev_image /bin/bash

- [Docker](#docker)
  - [Docker installation](#docker-installation)
  - [Docker Compose](#docker-compose)
  - [Docker testing](#docker-testing)
  - [VSCode + docker](#vscode--docker)
- [Vagrant (virtual machine)](#vagrant-virtual-machine)
- [WSL](#wsl)
  - [Issues](#issues)
  - [GUI apps even with older windows version than 10.0.21367.1000](#gui-apps-even-with-older-windows-version-than-100213671000)
  - [VSCode + WSL](#vscode--wsl)

# Docker
Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.

A Docker  **image**  is a file used to execute code in a Docker  **container** . Docker  **images**  act as a set of instructions to build a Docker  **container** , like a template. When the  **image**  is deployed to a Docker environment, it can be executed as a Docker  **container**  i.e. running image called container.

Docker images have multiple layers, each one originates from the previous layer but is different from it. The layers speed up Docker builds while increasing reusability and decreasing disk use. Image layers are also read-only files. Once a container is created, a writable layer is added on top of the unchangeable images, allowing a user to make changes.

 **Play with docker online:** [https://www.docker.com/play-with-docker](https://www.docker.com/play-with-docker)


## Docker installation

```bash
sudo snap install docker
# to run docker without sudo
sudo groupadd docker
sudo usermod -aG docker $USER
# restart your computer
docker run hello-world # test docker installation
```
for more details visit [https://docs.docker.com/engine/install/linux-postinstall/](https://docs.docker.com/engine/install/linux-postinstall/)

DockerfileA  **Dockerfile**  is a text document that contains all the commands you could call on the command line to make an image.


```bash
# get an image from https://hub.docker.com/
FROM ubuntu:20.04
# commands to run on the obtained image
RUN apt -y update
RUN apt install -y git-lfs
```

```bash
docker build -t test_image .
docker run -p 8888:8888 test_image # -p maps ports from the image to the hosting OS
docker run -it test_image # i: run interactivly, t: allocates pseudo-tty
docker run -it --name new_container test_image /bin/bash # name the container and run bash
docker container attach new_container # to reattach to a running container
docker run -dt test_image /bin/bash # run in deattached mode and keep running because bash is running in the container
docker exec -ti container_id /bin/bash # to get a shell on a running container
```

```bash
docker image history test_image # to see image layers                                                                         
# to push an image to dockerhub
docker login --username $dockerId
docker image tag test_image $dockerId/test_image:v1
docker image push $dockerId/test_image:v1                                           
```

## Docker Compose
If you want to run an application using multiple docker images or want to configure how to run a docker image using a configuration file instead of long commands in the terminal, you should use  **docker-compose** . Docker compose in configured using a docker-compose.yml

```bash
services:
  mycontainer:
    image: test_image
    build: .
	command: ls
    volumes:
      - ./src_host:/src_docker
    ports:
      - 8888:8888
```
To run the configured container, execute docker-compose up
volumes: ./[src:/src](http://src/src): mounts the src folder from the host to an src folder in the container
e.g.: `docker-compose up --force-recreate --build -d`


## Docker testing
To have an idea about used container run the code below

```bash
docker container ls -a # list containers
docker image ls -a # list images
docker volume ls -a # list volumes
docker network ls
```

After a bit of testing, it may be useful to stop and delete all docker containers via
```bash
docker stop $(docker ps -aq)
docker system prune # remove all stopped containers, dangling images, and unused networks
docker system prune --volumes # DANGER! remove data folders
```

## VSCode + docker
use devcontainer.json to configure vscode to use a docker container as a development environment
from within vscode, ctrl+shift+p, type reopen folder in container
use `docker init` to create the dockerfile

# Vagrant (virtual machine)
Vagrant is a tool for building and managing virtual machine environments in a single workflow. [https://www.vagrantup.com/intro](https://www.vagrantup.com/intro)

Similar to docker, vagrant is controlled via a  **Vagrantfile** 


```bash
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64" # more on https://app.vagrantup.com/boxes/search
  config.vm.provision :shell, path: "bootstrap.sh"
end
# ubuntu: user: vagrant password: vagrant
```
The virtual machine is created and started via vagrant up then it may be accessed via vargrant ssh or using VirtualBox GUI
The directory containing Vagrantfile is mounted as /vagrant
vagrant destroy → stop virtual machine and remove its disk
vagrant box list → show available boxes

# WSL
wsl --set-default-version 2
wsl --set-version Ubuntu 2
Wsl - l -v

wsl --list --online
wsl --install --distribution Ubuntu

## Issues
https://community.cisco.com/t5/vpn/anyconnect-wsl-2-windows-substem-for-linux/td-p/4179888
https://github.com/microsoft/WSL/issues/9867


## [GUI apps even with older windows version than 10.0.21367.1000](https://github.com/microsoft/wslg/wiki/Diagnosing-%22cannot-open-display%22-type-issues-with-WSLg)
cmd -> ver -> Microsoft Windows [Version 10.0.19045.2728]


install `VcXsrv Windows X Server`
disable access control & additional parameters `-ac` (maybe the same)
Windows Security -> Firewall & network protection -> Allow an app through firewall -> make sure VcXsrv has both public and private checked.

in WSL, use any of the following (easier than running ipconfig in cmd to check WSL ip ), put it in ~/.bashrc
```bash
export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"

export DISPLAY="`sed -n 's/nameserver //p' /etc/resolv.conf`:0"

export DISPLAY=$(ip route|awk '/^default/{print $3}'):0.0

sudo apt install x11-apps
xeyes
# export DISPLAY=10.166.73.180:0.0
# set DISPLAY=10.166.73.180:0.0  
```

https://github.com/microsoft/wslg/wiki/Diagnosing-%22cannot-open-display%22-type-issues-with-WSLg
https://stackoverflow.com/questions/60284542/wsl-gedit-unable-to-init-server-could-not-connect-connection-refused


## VSCode + WSL
from within vscode, ctrl+shift+p, type reopen folder in wsl

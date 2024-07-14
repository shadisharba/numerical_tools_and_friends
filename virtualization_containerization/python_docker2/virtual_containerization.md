# Python Development Environments

## docker

- Docker is a platform that allows you to package your application and its dependencies into a container.
- It provides a consistent and reproducible environment for your application.
- You can create a Docker image using a Dockerfile that specifies the environment and dependencies.
- Docker is recommended for projects that require consistent deployment across different environments.

### Dockerfile
For Dockerfile, there are some commands that are commonly used,

`FROM` is used once at the start of Dockerfile to indicate which base image to use, for our case we would want to use a base image that supports Python
`ARG` defines variables that users pass in at build-time. In the example below, port is an argument to be passed in when building a Docker image
`USER` sets username or user group when running Docker image
`COPY` copies files and directories to the container
`WORKDIR` sets the working directory of the container
`ENV` sets environment variable
`RUN` runs shell command, which calls `/bin/sh -c on Linux`
`EXPOSE` informs Docker that the container listens on the specified network ports at runtime, used for testing Docker applications locally
`CMD` is used once at the end of Dockerfile and contains the final command to run execute the container

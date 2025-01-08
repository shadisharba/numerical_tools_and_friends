#The base image for the container 
FROM python:3.9-slim-buster 
RUN apt update -qq && apt install -qq -y xvfb x11-apps

# Keeps Python from generating .pyc files in the container 
ENV PYTHONDONTWRITEBYTECODE=1 

# Turns off buffering for easier container logging 
ENV PYTHONUNBUFFERED=1 

# Copy all files to the docker container and install
WORKDIR /workspaces
COPY . /workspaces
RUN python -m pip install -r requirements.txt 

# Creates a non-root user with an explicit UID and adds permission to access the /workspaces folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /workspaces
USER appuser

ENV DISPLAY="192.168.178.46:0"
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "main.py"]
CMD ["xeyes"]

# ARG port
# EXPOSE $PORT
# --build-arg port=8060
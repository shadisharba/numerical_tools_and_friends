<!-- Docker isolates all content, code, and data in a container from your local filesystem.

Sometimes you may want the container to access a directory on your system. This is when you use bind mounts. -->

git clone https://github.com/docker/bindmount-apps
cd bindmount-apps

volumes: 
    - ./app:/usr/src/app
    - /usr/src/app/node_modules

<!-- The volumes element tells Compose to mount the local folder ./app to /usr/src/app in the container for the todo-app service. This particular bind mount overwrites the static contents of the /usr/src/app directory in the container and creates what is known as a development container. The second instruction, /usr/src/app/node_modules, prevents the bind mount from overwriting the container's node_modules directory to preserve the packages installed in the container. -->

docker compose up -d
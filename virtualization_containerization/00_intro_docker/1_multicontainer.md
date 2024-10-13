git clone https://github.com/docker/multi-container-app
cd multi-container-app
docker compose up -d

http://localhost:3000/

<!-- When developing with Docker, you may need to automatically update and preview your running services as you edit and save your code. We use docker compose watch for this.
Run the following command to run your project with compose watch. -->
docker compose watch
<!-- You can stop watch with Ctrl + C shortcut. -->
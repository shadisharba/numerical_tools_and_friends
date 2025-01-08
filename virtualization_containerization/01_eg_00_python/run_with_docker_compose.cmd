@echo off
@REM docker compose build
docker compose up --build

@REM <!-- When developing with Docker, you may need to automatically update and preview your running services as you edit and save your code. We use docker compose watch for this.
@REM Run the following command to run your project with compose watch. -->
@REM docker compose watch
@REM <!-- You can stop watch with Ctrl + C shortcut. -->
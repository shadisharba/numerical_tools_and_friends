IMAGER_NAME=myimage
DOCKER_SERVICE=01_eg_00_python
help:
	cat makefile
docker:
	docker build -t $(IMAGER_NAME) --progress plain .
	docker run -e DISPLAY=$(DISPLAY) -v /tmp/.X11-unix:/tmp/.X11-unix -it $(IMAGER_NAME)
compose:
	# xhost +local:root # allow root to access the display & not needed if you run as a standard user
	docker compose up --build -d --remove-orphans && docker compose run $(DOCKER_SERVICE) && docker compose down
	# xhost -local:root
compose_up:
	docker compose up
compose_exec:
	docker compose exec $(DOCKER_SERVICE) bash
# to be used in the container
test_gui:
	echo $(DISPLAY) && xeyes
test_jupyter:
	# activate environment before running jupyter
	jupyter-lab --port=8888 --no-browser --ip=0.0.0.0 --allow-root
test_github_actions:
	curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
	./bin/act --action-offline-mode -l
	./bin/act --action-offline-mode --graph
	./bin/act --action-offline-mode
	# rm ~/.config/act/actrc

	# act --job <name-of-your-job>
	# act --env-file=my-custom.env
	# act --secret-file=my-custom.secrets
	# act pull_request
.FORCE:

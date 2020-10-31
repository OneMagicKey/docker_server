.PHONY: build clean start stop healthcheck

build: Dockerfile
	docker build -t my_server .
	
start: build
	docker run my_server

start_interact: build
	docker run -it --entrypoint=/bin/bash my_server
		
stop: 
	docker stop $(shell docker ps -q --filter ancestor='my_server')
	
healthcheck:
	@if ! type "docker" > /dev/null; then\
  		echo You should install dot;\
  	else\
  		echo "Docker found!";\
	fi

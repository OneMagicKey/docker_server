.PHONY: build clean start stop healthcheck

build: Dockerfile
	mkdir logs
	docker build -t my_server .
	
start: build
	docker run -d my_server --volume $(shell pwd)/logs:/var/log -p 8080:8080

start_interact: build
	docker run -it --volume $(shell pwd)/logs:/var/log -p 8080:8080 --entrypoint=/bin/bash my_server 

clean:
	rm -rf logs
	docker rm $(shell docker ps -a --format="{{.Image}} {{.ID}}" | grep 'my_server' | cut -d' ' -f2)
	docker rmi $(shell docker images --format="{{.Repository}} {{.ID}}" | grep 'my_server' | cut -d' ' -f2)
	
			
stop: 
	docker stop $(shell docker ps -q --filter ancestor='my_server')
	
healthcheck:
	@if ! type "docker"; then\
  		echo You should install docker 1>&2;\
  	else\
  		echo "Docker found!";\
	fi

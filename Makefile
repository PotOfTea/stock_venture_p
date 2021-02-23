.DEFAULT_GOAL := run

ifeq (, $(shell which docker))
$(error "No docker in $(PATH), consider checking out https://http://docker.io/ for info")
endif


kubectl ?= kubectl
docker  ?= docker

build:
	$(docker) build -t stock_app .

run: build
	$(docker) run -d --name stock_app -p 80:80 stock_app
	@echo "App can be accessed from http://127.0.0.1:80"

delete:
	$(docker) rm -f stock_app

deploy:
	$(kubectl) apply -f deployment.yaml

undeploy:
	$(kubectl) delete -f deployment.yaml

test:
	- test -d venv || virtualenv venv
	- . venv/bin/activate; pip install -Ur requirements.txt
	pytest -v

port-forward:
	@echo "App can access on 127.0.0.1:8000"
	$(kubectl) -n stock port-forward service/stock-app 8000:80


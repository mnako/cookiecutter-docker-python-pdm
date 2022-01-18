USER_ID := $(shell id -u)
GROUP_ID := $(shell id -g)

dev-env:
	@if [ "$(shell docker image inspect --format='exists' {{ cookiecutter.project_name }}:dev)" != "exists" ]; then docker build --build-arg USER_ID=${USER_ID} --build-arg GROUP_ID=${GROUP_ID} --tag {{ cookiecutter.project_name }}:dev .; fi;
	@if [ ! -d "__pypackages__" ]; then docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm install; docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm install --group dev; fi;

run: dev-env
	docker run --rm -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev

bash: dev-env
	docker run -it -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev bash

format: dev-env
	@docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm run black .

test: dev-env
	@docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm run pytest --cov={{ cookiecutter.project_name }} tests
	@docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm run mypy
	@docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm run black --check .

build:
	@if [ -z ${VERSION} ]; then echo Usage: make build-production VERSION=0.0.0 && exit 1; fi;
	docker build --file Dockerfile.production --tag {{ cookiecutter.project_name }}:latest .
	docker tag {{ cookiecutter.project_name }}:latest {{ cookiecutter.project_name }}:${VERSION}

push:
	@if [ -z ${VERSION} ]; then echo Usage: make push-production VERSION=0.0.0 && exit 1; fi;
	docker tag {{ cookiecutter.project_name }}:latest ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:latest
	docker tag {{ cookiecutter.project_name }}:latest ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:${VERSION}
	docker push ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:latest
	docker push ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}:${VERSION}

rm:
	docker rm {{ cookiecutter.project_name }} || true
	docker rmi --force {{ cookiecutter.project_name }}:dev || true
	docker rmi --force {{ cookiecutter.project_name }}:latest || true
	rm -rf .mypy_cache/ || true
	rm -rf .pytest_cache/ || true
	rm -rf __pypackages__/ || true
	rm -rf tests/__pycache__/ || true

.PHONY: dev-env run bash format test build push rm
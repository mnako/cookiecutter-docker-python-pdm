build-dev:
	docker build --tag {{ cookiecutter.project_name }}:dev .

install-dev-deps:
	@docker run -it -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm install
	@docker run -it -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm install --group dev

run:
	@docker run --rm -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev

bash:
	docker run -it -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev bash

format:
	@docker run -it -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm run black .

test:
	@docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm run pytest --cov={{ cookiecutter.project_name }} tests
	@docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm run mypy
	@docker run -t -v "$(PWD):/app" {{ cookiecutter.project_name }}:dev pdm run black --check .

ci:
	docker run --rm --name {{ cookiecutter.project_name }} -t {{ cookiecutter.project_name }}:dev pdm run pytest --cov={{ cookiecutter.project_name }} tests
	docker run --rm --name {{ cookiecutter.project_name }} -t {{ cookiecutter.project_name }}:dev pdm run mypy
	docker run --rm --name {{ cookiecutter.project_name }} -t {{ cookiecutter.project_name }}:dev pdm run black --check .

build-production:
	@if [ -z ${VERSION} ]; then echo Usage: make build-production VERSION=0.0.0 && exit 1; fi;
	docker build --file Dockerfile.production --tag {{ cookiecutter.project_name }}:latest .
	docker tag {{ cookiecutter.project_name }}:latest {{ cookiecutter.project_name }}:${VERSION}

push-production:
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

# cookiecutter-docker-python-pdm

![CI Status](https://github.com/mnako/cookiecutter-docker-python-pdm/actions/workflows/ci.yml/badge.svg?branch=main)

A template for a Python project with a disposable, Docker-contained development
environment.

This cookiecutter gives you a Python 3.10 development environment with nice 
defaults:

* Python 3.10 with PDM package manager
* Pytest tests with a required coverage;
* Mypy tests
* Black formatter
* Dev Docker image
* Production Docker image
* CI/CD using Github actions

and depends on Docker and Makefile only.

## Quickstart

You can generate a new project by:

	pip install cookiecutter 
	cookiecutter gh:mnako/cookiecutter-docker-python-pdm

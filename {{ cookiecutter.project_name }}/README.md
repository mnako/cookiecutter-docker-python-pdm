{{ cookiecutter.project_name }}
====

Welcome to {{ cookiecutter.project_name }}

##  Quickstart guide:

1. Build dev Docker image:

   make build-dev

2. Install dev dependencies:
    
   make install-dev-deps

3. Run application:
    
   make run

4. Run formatter:

   make format

5. Test:

   make test

6. Build production image:

   make build-production VERSION=0.0.1

7. Push production image:

   make push-production VERSION=0.0.1

8. Remove development environment:

   make rm

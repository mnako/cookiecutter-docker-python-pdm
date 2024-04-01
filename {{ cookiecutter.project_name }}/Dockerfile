FROM python:3.11.7-slim-bookworm

ARG USER_ID
ARG GROUP_ID

LABEL org.opencontainers.image.source="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}"

RUN groupadd --force --gid ${GROUP_ID} --system usergroup && \
    useradd --uid ${USER_ID} --gid ${GROUP_ID} --create-home --system user && \
    mkdir /app && \
    chown user /app
USER user

WORKDIR /app
RUN python -m pip install --upgrade pip==24.0 && pip install --user pdm==2.13.0
ENV PATH="/app/__pypackages__/3.11/bin:/home/user/.local/bin:${PATH}"

COPY main.py pdm.lock pyproject.toml /app/
RUN pdm install
RUN pdm install --group dev --dev

ADD {{ cookiecutter.project_name }} /app/{{ cookiecutter.project_name }}
ADD tests /app/tests

CMD ["pdm", "run", "python", "main.py"]

import os
import pytest
import subprocess
import time
import logging

from cookiecutter import utils
from cookiecutter.main import cookiecutter


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("cookiecutter-docker-python-pdm")

test_project_dir = "/tmp/testproject"


@pytest.fixture(scope="session", autouse=True)
def test_project(request):
    """
    This fixture provides a test project to test cases.
    It cookiecuts a project with the config below, runs the test and removes
    the project directory.
    """

    def remove_generated_project():
        if os.path.isdir(test_project_dir):
            try:
                utils.rmtree(test_project_dir)
            except PermissionError:
                pass

    request.addfinalizer(remove_generated_project)

    cookiecutter(
        ".",
        output_dir="/tmp",
        no_input=True,
        extra_context={
            "github_username": "mnako",
            "project_name": "testproject"
        },
    )


def test_project_renders_to_dir(caplog):
    caplog.set_level(logging.INFO)

    assert os.path.isdir(test_project_dir)
    assert (
        "Lock file hash doesn't match pyproject.toml, packages may be outdated"
        not in caplog.text
    )


def test_project_make_run_succeeds():
    # caplog.set_level(logging.INFO)

    make_test_process = subprocess.Popen(
        "make run",
        shell=True,
        cwd=test_project_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for line in iter(make_test_process.stdout.readline, b""):
        logger.info(line.decode().strip())
        print(line.decode().strip())

    for line in iter(make_test_process.stderr.readline, b""):
        logger.warning(line.decode().strip())
        print(line.decode().strip())

    make_test_process_return_code = make_test_process.wait()
    assert (
        make_test_process_return_code == 0
    ), "make run did not exit with code 0"


def test_project_make_format_succeeds(caplog):
    caplog.set_level(logging.INFO)

    make_test_process = subprocess.Popen(
        "make format",
        shell=True,
        cwd=test_project_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for line in iter(make_test_process.stdout.readline, b""):
        logger.info(line.decode().strip())

    for line in iter(make_test_process.stderr.readline, b""):
        logger.warning(line.decode().strip())

    make_test_process_return_code = make_test_process.wait()
    assert (
            make_test_process_return_code == 0
    ), "make format did not exit with code 0"


def test_project_make_test_succeeds(caplog):
    caplog.set_level(logging.INFO)

    make_test_process = subprocess.Popen(
        "make test",
        shell=True,
        cwd=test_project_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for line in iter(make_test_process.stdout.readline, b""):
        logger.info(line.decode().strip())

    for line in iter(make_test_process.stderr.readline, b""):
        logger.warning(line.decode().strip())

    make_test_process_return_code = make_test_process.wait()
    assert (
        make_test_process_return_code == 0
    ), "make test did not exit with code 0"


def test_project_make_build_succeeds(caplog):
    caplog.set_level(logging.INFO)

    make_test_process = subprocess.Popen(
        "make build VERSION=0.0.0",
        shell=True,
        cwd=test_project_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for line in iter(make_test_process.stdout.readline, b""):
        logger.info(line.decode().strip())

    for line in iter(make_test_process.stderr.readline, b""):
        logger.warning(line.decode().strip())

    make_test_process_return_code = make_test_process.wait()
    assert (
        make_test_process_return_code == 0
    ), "make build VERSION=0.0.0 did not exit with code 0"
    assert (
        "Lock file hash doesn't match pyproject.toml, packages may be outdated"
        not in caplog.text
    )


def test_project_make_rm_succeeds(caplog):
    caplog.set_level(logging.INFO)

    make_test_process = subprocess.Popen(
        "make rm",
        shell=True,
        cwd=test_project_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for line in iter(make_test_process.stdout.readline, b""):
        logger.info(line.decode().strip())

    for line in iter(make_test_process.stderr.readline, b""):
        logger.warning(line.decode().strip())

    make_test_process_return_code = make_test_process.wait()
    assert (
        make_test_process_return_code == 0
    ), "make rm did not exit with code 0"

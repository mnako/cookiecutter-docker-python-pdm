import pytest

from {{ cookiecutter.project_name }}.functions import say_hi


@pytest.mark.parametrize(
    "name, expected_salutation",
    [("Docker", "Hi, Docker"), ("Python", "Hi, Python"), ("PDM", "Hi, PDM")],
)
def test_say_hi(name: str, expected_salutation: str) -> None:
    assert say_hi(name) == expected_salutation

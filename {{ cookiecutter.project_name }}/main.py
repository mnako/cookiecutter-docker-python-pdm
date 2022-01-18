from {{ cookiecutter.project_name }}.functions import say_hi


if __name__ == "__main__":
    print(say_hi("Docker"))

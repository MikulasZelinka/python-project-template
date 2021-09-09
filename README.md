# python project template

A minimal, slightly opinionated template for Python projects.

Includes convenient configuration (everything is in [pyproject.toml]) and automatic checks ([pre-commit config]).

## usage

1. [Install](https://python-poetry.org/docs/#installation) [poetry] and `cd` to this folder.

2. `poetry install`

3. `poetry run pre-commit install`

You are now ready to [run your project using poetry](https://python-poetry.org/docs/basic-usage/#using-poetry-run):

```shell
poetry run python your_script.py
```

Alternatively, you can
[activate your env's shell](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)
to run any relevant commands in your env:

```shell
poetry shell
> pip list
> python first_script.py
> python second_script.py
```

## approach

- [poetry] as the main package manager/runner
- [black] – code formatting ([compatible configs](https://github.com/psf/black/tree/main/docs/compatible_configs))
- [isort] – import formatting
- [flake8] – linting ([pflake8] is used as a wrapper that supports [pyproject.toml])
- [pytest] – testing
- [pre-commit] to run all above automa[tg]ically

## guidelines

### dependencies, building, publishing

See the [poetry docs](https://python-poetry.org/docs/basic-usage/).

### coding style and formatting

As dictated by [black], [isort] and [flake8].

Set and configured in [pyproject.toml].

### docstrings

Use the [Google docstring style](https://google.github.io/styleguide/pyguide#38-comments-and-docstrings)
([all-in-one example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)).

Most IDEs should support it out of the box
([PyCharm](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000218290-Configure-google-docstring),
[VSCode](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)).

### logging

It is recommended to use [loguru].

Additional resources:

- https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/

---

## todo

- [coverage]
- [mypy]
- [sphinx] ([Read the Docs]) for automatic documentation generation
- spellchecker ([codespell](https://github.com/codespell-project/codespell)?)
- [poetry] IDE support:
    - [PyCharm plugin](https://plugins.jetbrains.com/plugin/14307-poetry),
      [official ticket](https://youtrack.jetbrains.com/issue/PY-30702)
- GitHub actions (CI)
    - e.g., run the (pre-)commit checks there
- ~~logging template~~
    - likely not needed thanks to the [loguru] preference over the standard python `logging` module
- [cookiecutter]
    - consider turing this into a cookiecutter template
      (or at least have that as a version, perhaps it's a bit clearer without the template)
    - examples:
        - https://github.com/johanvergeer/cookiecutter-poetry
        - https://github.com/audreyfeldroy/cookiecutter-pypackage
        - https://github.com/sourcery-ai/python-best-practices-cookiecutter

### References

- https://github.com/pronovic/apologies
- https://github.com/rochacbruno/python-project-template


[poetry]: https://github.com/python-poetry/poetry
[black]: https://github.com/psf/black
[isort]: https://github.com/PyCQA/isort
[flake8]: https://github.com/PyCQA/flake8
[pflake8]: https://github.com/csachs/pyproject-flake8
[pytest]: https://docs.pytest.org
[pre-commit]: https://pre-commit.com/

[loguru]: https://github.com/Delgan/loguru

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[coverage]: https://coverage.readthedocs.io
[mypy]: https://github.com/python/mypy
[sphinx]: https://www.sphinx-doc.org/en/master/
[Read the Docs]: https://readthedocs.org/

[pyproject.toml]: pyproject.toml
[pre-commit config]: .pre-commit-config.yaml

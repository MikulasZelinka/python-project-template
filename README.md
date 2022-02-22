# Python project template

A minimal, slightly opinionated template for Python projects.

Includes convenient configuration (everything is in [pyproject.toml]) and automatic checks ([pre-commit config]).

## Setup

0. (optional) If you require packages only provided by `conda`, first install and activate the conda environment
   (refer to the [conda directory](conda)).

2. [Install](https://python-poetry.org/docs/#installation) [poetry] and `cd` to this folder.

3. `poetry install`

4. `poetry run pre-commit install`

You are now ready to [run your project using poetry](https://python-poetry.org/docs/basic-usage/#using-poetry-run).


## Usage

### Running your python code

```shell
poetry run python your_script.py
```

Alternatively, you can
[activate your project env's shell](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)
to run any relevant commands in your env:

```shell
poetry shell
> pip list
> python first_script.py
> python second_script.py
```

### Managing dependencies

Adding a dependency is as simple as running [`add`](https://python-poetry.org/docs/cli/#add)
```shell
poetry add loguru
```

The dependency will then automatically be added to your [pyproject.toml],
although you can also [work with pyproject.toml directly](https://python-poetry.org/docs/basic-usage/#specifying-dependencies).

There's many more useful features (like dependency grouping), please see the
[poetry docs](https://python-poetry.org/docs/dependency-specification/).

### Git workflow

Whenever you try to `git commit`, the [pre-commit config] hooks
will automatically run [the tools mentioned](#approach).

Note that they only run on your currently `staged` files (see `git status`).
Your unstaged files will be automatically stashed for the pre-commit run, and then unstashed back.
This just means that the check is run against the file state that would actually
appear in the repository if the commit succeeded.

- If there are no changes (formatting) or problems (linting, testing) during the process,
the commit will simply succeed.

- If there are changes or linting or testing fails, the commit fails,
  optionally updating your files in the process (`black`, `isort`)
    - In order to then try again, first stage the changed files iff the changes look good:
      - `git add -u` - to add only modified but unstaged files
    - And then you can commit again, now the changes are taken into account: `git commit`

If for some reason you want to skip the pre-commit checks, you can do so with `git commit -n`
(where `-n` is a shortcut for `--no-verify`).
However, this is usually not advised.

In the future, we would like to have these automatic hook checks set up in our GitHub CI,
so that they'd be automatically run for pull requests as well.

## Approach

- [poetry] as the main package manager/runner
- [black] – code formatting ([compatible configs](https://github.com/psf/black/tree/main/docs/compatible_configs))
- [isort] – import formatting
- [flake8] – linting ([pflake8] is used as a wrapper that supports [pyproject.toml])
- [pytest] – testing
- [pre-commit] to run all above automa[tg]ically

## Guidelines

### Dependencies, building, publishing

See the [poetry docs](https://python-poetry.org/docs/basic-usage/).

### Coding style and formatting

As dictated by [black], [isort] and [flake8].

Set and configured in [pyproject.toml].

### Docstrings

Use the [Google docstring style](https://google.github.io/styleguide/pyguide#38-comments-and-docstrings)
([all-in-one example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)).

Most IDEs should support it out of the box
([PyCharm](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000218290-Configure-google-docstring),
[VSCode](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)).

### Logging

It is recommended to use [loguru].

Additional resources:

- https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/

---

## TODO

- [ ] [mypy]
- [ ] [tox] with [conda support](https://github.com/tox-dev/tox-conda)
- [ ] [GitHub Actions]
- [ ] [coverage]
- [ ] [mypy]
- [ ] [sphinx] ([Read the Docs]) for automatic documentation generation
- [ ] Decide on `tests` structure: top-level vs scattered across the repo
- [ ] spellchecker ([codespell](https://github.com/codespell-project/codespell)?)
- [ ] [poetry] IDE support:
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
[tox]: https://github.com/tox-dev/tox
[GitHub Actions]: https://github.com/features/actions

[pyproject.toml]: pyproject.toml
[pre-commit config]: .pre-commit-config.yaml

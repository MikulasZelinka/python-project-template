# ppt

ppt – python project template

## setup

1. Install poetry and `cd` to this folder.

2. `poetry install`

3. `poetry run pre-commit install`

## approach

- poetry as the main package manager/runner
- black, isort (code formatting)
- flake8 (linting)
- pre-commit (to automatically run all the above)

## todo

- logging template
- python comment style
- coverage
- formalise [setup](#setup) (makefile?)
- [cut this into cookies](https://github.com/cookiecutter/cookiecutter)?
- integrate into an IDE (PyCharm)
- GitHub actions

## resources

Useful links, repos, etc.:

- https://github.com/pronovic/apologies
- https://github.com/huggingface/transformers
- https://github.com/psf/black, [compatible configs](https://github.com/psf/black/tree/master/docs/compatible_configs)
- https://github.com/sourcery-ai/python-best-practices-cookiecutter
- https://github.com/audreyfeldroy/cookiecutter-pypackage
- https://github.com/johanvergeer/cookiecutter-poetry

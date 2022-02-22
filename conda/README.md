# Using poetry inside a conda env

If you don't need to use any conda packages, you can ignore this directory.

If conda packages (and thus an env) are necessary, then follow these instructions and examples.

## New project setup

1. Create a project-specific conda env:

Modify constants and required packages in [`bootstrap.sh`](bootstrap.sh) and run it.

## Existing project setup

1. Create a conda env from the existing `environment.yaml` file:

```shell
conda env create -f conda/python-project-template.yaml
```

2. Activate the env:

```shell
conda activate python-project-template
```

## Usage

Once you've set up and activated the conda env, you can simply [use poetry as you would normally](../#Usage).
It will respect and use the currently activated conda env and even install (pip) packages to it.

For example, `pip list` will list the packages installed by poetry and pip,
and `conda list` will list both conda as well as poetry/pip packages saying which comes from which source.

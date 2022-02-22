"""Dummy pytest test(s) to allow the pre-commit test pipeline to work without any real tests."""

import pytest


def test_pytest_version_available():
    """Print pytest's version (doh)."""
    print(pytest.__version__)

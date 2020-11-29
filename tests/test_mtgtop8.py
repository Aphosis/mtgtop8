# pylint: disable=missing-module-docstring, missing-function-docstring
from mtgtop8 import __version__


def test_version():
    assert __version__ == "0.1.0"

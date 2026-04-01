
from isort.deprecated.finders import LocalFinder
import pytest

def test_valid_input_with_period():
    finder = LocalFinder(config=None)  # Passing a default value for config
    assert finder.find(".mymodule") == "LOCALFOLDER"
    assert finder.find("mymodule") is None

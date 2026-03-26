
from pathlib import Path

import pytest

from isort.main import _preconvert


def test_valid_input_path():
    test_path = Path('somefile.txt')
    result = _preconvert(test_path)
    assert isinstance(result, str), "Expected a string representation of the path"
    assert result == str(test_path), "The string representation should be equal to the path's absolute string"

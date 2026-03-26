
import pytest
from isort.main import _preconvert
from pathlib import Path
from enum import Enum

def test_invalid_input_dict():
    test_dict = {'key': 'value'}
    with pytest.raises(TypeError) as excinfo:
        _preconvert(test_dict)
    assert str(excinfo.value) == f"Unserializable object {test_dict} of type <class 'dict'>"

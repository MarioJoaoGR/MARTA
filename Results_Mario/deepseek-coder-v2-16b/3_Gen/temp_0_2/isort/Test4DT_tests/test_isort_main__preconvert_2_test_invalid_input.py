
import pytest
from isort.main import _preconvert
from pathlib import Path

def test_invalid_input():
    non_serializable = 'not serializable'
    with pytest.raises(TypeError) as e:
        _preconvert(non_serializable)
    assert str(e.value) == f"Unserializable object not serializable of type {type(non_serializable)}"

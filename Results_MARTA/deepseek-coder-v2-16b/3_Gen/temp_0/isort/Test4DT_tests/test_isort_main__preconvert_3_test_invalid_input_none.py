
import pytest

from isort.main import _preconvert


def test_invalid_input_none():
    with pytest.raises(TypeError) as excinfo:
        _preconvert(None)
    assert str(excinfo.value) == "Unserializable object None of type <class 'NoneType'>"

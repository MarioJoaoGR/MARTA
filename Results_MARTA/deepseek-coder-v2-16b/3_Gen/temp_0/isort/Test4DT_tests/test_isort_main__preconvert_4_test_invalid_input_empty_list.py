
import pytest

from isort.main import _preconvert


def test_invalid_input_empty_list():
    with pytest.raises(TypeError):
        _preconvert([])

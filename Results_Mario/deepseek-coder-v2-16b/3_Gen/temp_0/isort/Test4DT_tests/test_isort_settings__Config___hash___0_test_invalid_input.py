
import pytest
from isort.settings import _Config
from unittest.mock import patch

@pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        _Config(**{k: v for k, v in _Config.__annotations__.items() if k != 'py_version'})

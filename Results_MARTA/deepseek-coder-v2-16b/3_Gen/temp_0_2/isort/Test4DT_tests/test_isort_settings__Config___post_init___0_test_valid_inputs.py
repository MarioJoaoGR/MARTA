
import pytest
from isort.settings import _Config

def test_valid_inputs():
    config = _Config(py_version='3', line_length=80)
    assert config.line_length == 80
    assert isinstance(config, _Config)

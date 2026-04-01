
import sys

from isort.settings import _Config, stdlibs


def test_valid_inputs():
    config = _Config(py_version='3', line_length=80)
    
    # Check if the configuration object was created correctly
    assert config.py_version == 'py3'

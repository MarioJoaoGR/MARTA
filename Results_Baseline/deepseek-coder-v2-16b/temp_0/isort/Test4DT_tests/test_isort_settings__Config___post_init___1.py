
import sys

import pytest

from isort.settings import VALID_PY_TARGETS, WrapModes, _Config, stdlibs


# Test initialization with basic configuration
def test_basic_configuration():
    config = _Config(py_version='3', line_length=80)
    assert config.line_length == 80

# Test forcing imports to top
def test_force_to_top():
    config = _Config(py_version='3', force_to_top=frozenset(['sys']))
    assert config.force_to_top == frozenset(['sys'])

# Test customizing import wrapping
def test_customizing_import_wrapping():
    config = _Config(py_version='3', multi_line_output=WrapModes.VERTICAL_GRID)
    assert config.multi_line_output == WrapModes.VERTICAL_GRID

# Test alphabetical sorting
def test_alphabetical_sorting():
    config = _Config(py_version='3', force_alphabetical_sort=True)
    assert config.force_alphabetical_sort_within_sections is True
    assert config.no_sections is True
    assert config.lines_between_types == 1
    assert config.from_first is True

# Test handling unsupported Python version
def test_unsupported_python_version():
    with pytest.raises(ValueError) as excinfo:
        _Config(py_version='4', line_length=80)
    expected_message = f"The python version 4 is not supported. You can set a python version with the -py or --python-version flag. The following versions are supported: {VALID_PY_TARGETS}"
    assert str(excinfo.value) == expected_message

# Test wrap_length must be less than or equal to line_length
def test_wrap_length_must_be_less_than_or_equal_to_line_length():
    with pytest.raises(ValueError) as excinfo:
        config = _Config(py_version='3', wrap_length=100, line_length=80)
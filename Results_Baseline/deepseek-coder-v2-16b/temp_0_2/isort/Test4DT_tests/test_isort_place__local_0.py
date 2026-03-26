# Module: isort.place
import pytest

from isort import Config
from isort.place import LOCAL, _local


# Test case 1: Module name does not start with a dot
def test_module_name_does_not_start_with_dot():
    result = _local("module_name", Config())
    assert result is None

# Test case 2: Module name starts with a dot
def test_module_name_starts_with_dot():
    result = _local(".module_name", Config())
    expected_output = (LOCAL, "Module name started with a dot.")
    assert result == expected_output

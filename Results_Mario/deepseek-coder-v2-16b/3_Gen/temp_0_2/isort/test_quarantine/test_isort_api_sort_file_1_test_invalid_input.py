
import pytest
from pathlib import Path
from isort.api import sort_file
from isort import Config, DEFAULT_CONFIG
from io import TextIOWrapper
import sys
from typing import Any, TextIO

@pytest.mark.parametrize("filename", [None, 123, Path("")])
def test_invalid_input(filename):
    with pytest.raises(TypeError) as excinfo:
        sort_file(filename=filename)
    assert "Expected str or Path, got" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_sort_file_1_test_invalid_input
isort/Test4DT_tests/test_isort_api_sort_file_1_test_invalid_input.py:5:0: E0611: No name 'DEFAULT_CONFIG' in module 'isort' (no-name-in-module)


"""
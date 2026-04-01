
import pytest
from isort.api import sort_file
from pathlib import Path
import sys
from io import TextIOBase
from isort import Config, DEFAULT_CONFIG
from typing import Any
import io
import shutil

@pytest.mark.parametrize("filename", [None, 12345, True])
def test_invalid_inputs(filename):
    with pytest.raises(TypeError) as excinfo:
        sort_file(filename)
    assert "Expected str or Path, got" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_sort_file_0_test_invalid_inputs
isort/Test4DT_tests/test_isort_api_sort_file_0_test_invalid_inputs.py:7:0: E0611: No name 'DEFAULT_CONFIG' in module 'isort' (no-name-in-module)


"""
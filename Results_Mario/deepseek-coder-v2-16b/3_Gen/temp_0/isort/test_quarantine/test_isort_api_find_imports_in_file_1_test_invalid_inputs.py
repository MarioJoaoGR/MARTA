
from pathlib import Path
import pytest
from isort.api import find_imports_in_file
from isort.config import Config, DEFAULT_CONFIG
from warnings import warn

@pytest.mark.parametrize("filename", [None, "", "non_existent_file.py"])
def test_invalid_inputs(filename):
    with pytest.raises(OSError):
        list(find_imports_in_file(filename))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_find_imports_in_file_1_test_invalid_inputs
isort/Test4DT_tests/test_isort_api_find_imports_in_file_1_test_invalid_inputs.py:5:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_api_find_imports_in_file_1_test_invalid_inputs.py:5:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""
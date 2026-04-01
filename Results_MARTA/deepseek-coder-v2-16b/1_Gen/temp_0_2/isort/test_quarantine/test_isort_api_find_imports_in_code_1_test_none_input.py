
from io import StringIO
from pathlib import Path
from typing import Any, Iterator
import pytest
from find_imports_in_code import (
    Config, DEFAULT_CONFIG, ImportKey, find_imports_in_code, find_imports_in_stream
)

def test_none_input():
    code = None
    with pytest.raises(TypeError):
        list(find_imports_in_code(code))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_find_imports_in_code_1_test_none_input
isort/Test4DT_tests/test_isort_api_find_imports_in_code_1_test_none_input.py:6:0: E0401: Unable to import 'find_imports_in_code' (import-error)


"""
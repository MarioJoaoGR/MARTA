
import pytest
from typing import Optional, Any
from dataclasses_json.utils import _is_optional, _issubclass_safe, _hasargs

def test_valid_case_1():
    assert _is_optional(Optional[int]) == True
    assert _is_optional(Optional[str]) == True
    assert _is_optional(Any) == True
    assert _is_optional(int) == False
    assert _is_optional(List[int]) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_optional_0_test_valid_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_0_test_valid_case_1.py:11:24: E0602: Undefined variable 'List' (undefined-variable)

"""
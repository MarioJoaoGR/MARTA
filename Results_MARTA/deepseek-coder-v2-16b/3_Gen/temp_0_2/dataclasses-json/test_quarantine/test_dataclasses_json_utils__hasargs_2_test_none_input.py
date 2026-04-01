
import pytest
from typing import List, Tuple

def test_none_input():
    with pytest.raises(TypeError):
        _hasargs(int, None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__hasargs_2_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_2_test_none_input.py:7:8: E0602: Undefined variable '_hasargs' (undefined-variable)


"""
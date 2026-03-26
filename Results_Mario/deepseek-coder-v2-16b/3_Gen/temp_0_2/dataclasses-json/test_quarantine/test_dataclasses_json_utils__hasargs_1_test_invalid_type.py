
import pytest
from typing import List, Tuple

def test_invalid_type():
    with pytest.raises(TypeError):
        _hasargs(List[int], 1)  # Should raise TypeError because '1' is not a type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__hasargs_1_test_invalid_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_1_test_invalid_type.py:7:8: E0602: Undefined variable '_hasargs' (undefined-variable)


"""
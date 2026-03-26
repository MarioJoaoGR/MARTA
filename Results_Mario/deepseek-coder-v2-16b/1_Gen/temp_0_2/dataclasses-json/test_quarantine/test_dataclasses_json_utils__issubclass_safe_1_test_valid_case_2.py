
from dataclasses_json.utils import _issubclass_safe, _is_new_type, _is_new_type_subclass_safe
import pytest

@pytest.mark.parametrize("cls, classinfo, expected", [
    (B, A, True),  # B is a subclass of A
    (C, (A, B), False),  # C is not a subclass of A or B
    (D, C, True)  # D has __supertype__ attribute set to C, so it should be considered a subclass of C
])
def test_valid_case_2(_issubclass_safe, _is_new_type, _is_new_type_subclass_safe, cls, classinfo, expected):
    assert _issubclass_safe(cls, classinfo) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__issubclass_safe_1_test_valid_case_2
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_1_test_valid_case_2.py:6:5: E0602: Undefined variable 'B' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_1_test_valid_case_2.py:6:8: E0602: Undefined variable 'A' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_1_test_valid_case_2.py:7:5: E0602: Undefined variable 'C' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_1_test_valid_case_2.py:7:9: E0602: Undefined variable 'A' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_1_test_valid_case_2.py:7:12: E0602: Undefined variable 'B' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_1_test_valid_case_2.py:8:5: E0602: Undefined variable 'D' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_1_test_valid_case_2.py:8:8: E0602: Undefined variable 'C' (undefined-variable)


"""
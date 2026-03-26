
import pytest
from string_utils.manipulation import __StringFormatter

def test_edge_case_none():
    with pytest.raises(InvalidInputError) as excinfo:
        formatter = __StringFormatter(None)
    assert str(excinfo.value) == "'NoneType' object is not a valid string."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0_test_edge_case_none
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0_test_edge_case_none.py:6:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)


"""

import pytest
from string_utils.manipulation import booleanize

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        assert not booleanize('invalid')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_2_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_2_test_invalid_input.py:6:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)


"""
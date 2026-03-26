
import pytest
from string_utils.validation import InvalidInputError, NUMBER_RE

def test_error_handling():
    with pytest.raises(InvalidInputError):
        assert not is_number(123)  # This should raise an error because the input is not a string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_number_2_test_error_handling
python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_2_test_error_handling.py:7:19: E0602: Undefined variable 'is_number' (undefined-variable)


"""
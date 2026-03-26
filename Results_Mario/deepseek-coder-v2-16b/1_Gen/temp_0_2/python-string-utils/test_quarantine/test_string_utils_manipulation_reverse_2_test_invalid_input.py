
import pytest
from your_module import reverse, InvalidInputError  # Replace 'your_module' with the actual module name

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        assert reverse(123)  # This should raise InvalidInputError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_reverse_2_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation_reverse_2_test_invalid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""
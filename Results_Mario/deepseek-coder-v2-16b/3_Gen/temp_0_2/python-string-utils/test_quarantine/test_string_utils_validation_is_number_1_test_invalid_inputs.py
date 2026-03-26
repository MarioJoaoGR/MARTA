
import re
import pytest

# Assuming NUMBER_RE is defined somewhere in a module string_utils.validation
NUMBER_RE = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')

def test_invalid_inputs():
    # Test cases for invalid inputs
    invalid_inputs = ['1 2 3', 'abc', '', None]
    
    for input_string in invalid_inputs:
        with pytest.raises(ValueError):
            is_number(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_number_1_test_invalid_inputs
python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_1_test_invalid_inputs.py:14:12: E0602: Undefined variable 'is_number' (undefined-variable)


"""
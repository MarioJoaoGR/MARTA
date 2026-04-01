
import pytest
from string_utils.errors import InvalidInputError

def test_valid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        process_string("not a string")
    assert str(excinfo.value) == 'Expected "str", received "type not a string"'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_errors_InvalidInputError___init___0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0_test_valid_input.py:7:8: E0602: Undefined variable 'process_string' (undefined-variable)


"""
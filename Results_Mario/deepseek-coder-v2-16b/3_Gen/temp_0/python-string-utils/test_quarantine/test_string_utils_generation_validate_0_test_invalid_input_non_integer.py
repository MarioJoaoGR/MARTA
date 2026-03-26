
from string_utils.generation import validate
import pytest

def test_invalid_input_non_integer():
    with pytest.raises(ValueError) as excinfo:
        validate('not an int', 'number')
    assert str(excinfo.value) == '"number" must be an integer in the range 1-3999'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_validate_0_test_invalid_input_non_integer
python-string-utils/Test4DT_tests/test_string_utils_generation_validate_0_test_invalid_input_non_integer.py:2:0: E0611: No name 'validate' in module 'string_utils.generation' (no-name-in-module)


"""
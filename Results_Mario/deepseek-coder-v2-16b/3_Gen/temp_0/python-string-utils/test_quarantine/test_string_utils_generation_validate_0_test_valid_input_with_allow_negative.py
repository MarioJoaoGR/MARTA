
from string_utils.generation import validate
import pytest

def test_valid_input_with_allow_negative():
    # Test with a valid positive integer
    assert validate(25, 'number') is None
    
    # Test with a valid negative integer allowed by allow_negative=True
    with pytest.raises(ValueError) as excinfo:
        validate(-5, 'number', allow_negative=True)
    assert str(excinfo.value) == '"number" must be an integer in the range 1-3999'
    
    # Test with a non-integer value
    with pytest.raises(ValueError) as excinfo:
        validate('not an int', 'number')
    assert str(excinfo.value) == '"number" must be an integer in the range 1-3999'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_validate_0_test_valid_input_with_allow_negative
python-string-utils/Test4DT_tests/test_string_utils_generation_validate_0_test_valid_input_with_allow_negative.py:2:0: E0611: No name 'validate' in module 'string_utils.generation' (no-name-in-module)


"""

import pytest
from string_utils.generation import validate

def test_valid_input_happy_path():
    # Test with a valid positive integer within the range 1-3999
    assert validate(2500, 'year') is None
    
    # Test with a valid negative integer (converted to absolute value)
    assert validate(-5, 'age', allow_negative=True) is None
    
    # Test with an invalid positive integer outside the range 1-3999
    with pytest.raises(ValueError) as excinfo:
        validate(4000, 'year')
    assert str(excinfo.value) == '"year" must be an integer in the range 1-3999'
    
    # Test with an invalid negative integer outside the range 1-3999 (should raise ValueError)
    with pytest.raises(ValueError) as excinfo:
        validate(-4000, 'year')
    assert str(excinfo.value) == '"year" must be an integer in the range 1-3999'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_validate_0_test_valid_input_happy_path
python-string-utils/Test4DT_tests/test_string_utils_generation_validate_0_test_valid_input_happy_path.py:3:0: E0611: No name 'validate' in module 'string_utils.generation' (no-name-in-module)


"""
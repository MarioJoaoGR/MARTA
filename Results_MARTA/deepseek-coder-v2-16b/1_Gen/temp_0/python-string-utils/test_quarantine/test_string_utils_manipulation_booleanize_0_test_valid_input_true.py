
import pytest
from string_utils.manipulation import booleanize
from custom_exceptions import InvalidInputError

def test_valid_input_true():
    # Test with valid true inputs
    assert booleanize('true') is True
    assert booleanize('YES') is True
    assert booleanize('yEs') is True
    assert booleanize('1') is True
    assert booleanize('YeS') is True
    assert booleanize('Y') is True
    
    # Test with invalid true inputs
    assert booleanize('false') is False
    assert booleanize('no') is False
    assert booleanize('0') is False
    assert booleanize('nope') is False
    
    # Test with non-string input to trigger InvalidInputError
    with pytest.raises(InvalidInputError):
        booleanize(123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_0_test_valid_input_true
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_0_test_valid_input_true.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)

"""

import pytest
from string_utils.manipulation import booleanize
from custom_exceptions import InvalidInputError

def test_booleanize_edge_cases():
    # Test valid positive cases
    assert booleanize('true') == True
    assert booleanize('1') == True
    assert booleanize('yes') == True
    assert booleanize('y') == True
    
    # Test invalid positive cases
    assert booleanize('TRUE') == True  # Case insensitive test
    assert booleanize('Yes') == True   # Case insensitive test
    assert booleanize('NOPE') == False # Case insensitive test
    
    # Test negative case
    with pytest.raises(InvalidInputError):
        booleanize('invalid')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_6_test_edge_cases
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_6_test_edge_cases.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""
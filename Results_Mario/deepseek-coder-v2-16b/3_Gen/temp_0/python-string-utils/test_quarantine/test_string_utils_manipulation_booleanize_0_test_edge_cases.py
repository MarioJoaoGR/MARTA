
import pytest
from string_utils.manipulation import booleanize
from custom_exceptions import InvalidInputError

def test_booleanize_edge_cases():
    # Test cases for edge cases where input is not a string
    with pytest.raises(InvalidInputError):
        assert booleanize(None)  # None should raise an error
    with pytest.raises(InvalidInputError):
        assert booleanize(123)   # Integer should raise an error
    with pytest.raises(InvalidInputError):
        assert booleanize([])    # List should raise an error
    
    # Test cases for edge cases where input is a string but not one of the accepted values
    assert booleanize('false') == False  # 'false' should return False
    assert booleanize('no') == False     # 'no' should return False
    assert booleanize('0') == False      # '0' should return False
    assert booleanize('nope') == False   # 'nope' should return False
    
    # Test cases for edge cases where input is a string and it matches one of the accepted values
    assert booleanize('true') == True    # 'true' should return True
    assert booleanize('YES') == True     # 'YES' should return True
    assert booleanize('1') == True       # '1' should return True
    assert booleanize('y') == True       # 'y' should return True
    assert booleanize('Yes') == True     # 'Yes' should return True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_0_test_edge_cases
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_0_test_edge_cases.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""
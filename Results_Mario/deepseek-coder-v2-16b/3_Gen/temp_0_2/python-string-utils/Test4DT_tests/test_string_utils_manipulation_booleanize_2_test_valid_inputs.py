
import pytest
from string_utils.manipulation import booleanize

def test_valid_inputs():
    # Test cases where the input should return True
    assert booleanize('true') == True
    assert booleanize('1') == True
    assert booleanize('yes') == True
    assert booleanize('y') == True
    
    # Test cases where the input should return False
    assert booleanize('false') == False
    assert booleanize('0') == False
    assert booleanize('no') == False
    assert booleanize('n') == False
    
    # Case-insensitive tests
    assert booleanize('True') == True
    assert booleanize('TRUE') == True
    assert booleanize('YES') == True
    assert booleanize('Yes') == True
    assert booleanize('yEs') == True
    assert booleanize('False') == False
    assert booleanize('FALSE') == False
    assert booleanize('NO') == False
    assert booleanize('No') == False
    
    # Additional test cases to ensure robustness
    assert booleanize('tRue') == True
    assert booleanize('yES') == True
    assert booleanize('fAlse') == False
    assert booleanize('nO') == False

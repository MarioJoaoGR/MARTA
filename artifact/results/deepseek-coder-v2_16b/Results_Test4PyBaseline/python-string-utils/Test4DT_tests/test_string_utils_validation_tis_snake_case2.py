
import pytest
from string_utils.validation import is_snake_case

# Test cases for invalid snake case strings
def test_invalid_snake_case():
    # Test with an empty string
    assert not is_snake_case(''), "Expected False, but got True for an empty string"
    
    # Test with a single uppercase letter (should be invalid)
    assert not is_snake_case('Foo'), "Expected False, but got True for 'Foo'"
    
    # Test with a string that starts with a number (should be invalid)
    assert not is_snake_case('123foo'), "Expected False, but got True for '123foo'"
    
    # Test with a string containing uppercase letters and no separator (should be invalid)
    assert not is_snake_case('FooBarBaz'), "Expected False, but got True for 'FooBarBaz'"
    
    # Test with a string that contains special characters (should be invalid)
    assert not is_snake_case('foo@bar$baz'), "Expected False, but got True for 'foo@bar$baz'"

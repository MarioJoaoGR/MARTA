
import re
from unittest import mock
from string_utils.validation import is_snake_case

def test_error_case():
    # Test when input string is not a string
    assert not is_snake_case(12345)
    
    # Test when input string contains uppercase letters
    assert not is_snake_case('FooBarBaz')
    
    # Test when input string starts with a number
    assert not is_snake_case('1foo_bar_baz')
    
    # Test when input string does not contain the separator
    assert not is_snake_case('foobarbaz')
    
    # Test when input string contains only lowercase letters and digits
    assert is_snake_case('foo_bar_baz')
    
    # Test with a different separator
    assert is_snake_case('foo-bar-baz', '-')

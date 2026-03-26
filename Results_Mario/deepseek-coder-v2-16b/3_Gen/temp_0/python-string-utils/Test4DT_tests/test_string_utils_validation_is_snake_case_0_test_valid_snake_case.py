
import re
from string_utils.validation import is_snake_case

def test_valid_snake_case():
    # Test valid snake case strings with default separator '_'
    assert is_snake_case('foo_bar_baz') == True
    assert is_snake_case('foo_123_bar') == True
    assert is_snake_case('foo_bar') == True
    
    # Test valid snake case strings with custom separator '-'
    assert is_snake_case('foo-bar-baz', separator='-') == True
    assert is_snake_case('foo-123-bar', separator='-') == True
    assert is_snake_case('foo-bar', separator='-') == True
    
    # Test invalid snake case strings without the required separator
    assert is_snake_case('fooBarBaz') == False
    assert is_snake_case('foo123Bar') == False
    
    # Test invalid snake case strings with numbers at the start
    assert is_snake_case('123foo_bar') == False


import pytest
from string_utils.manipulation import camel_case_to_snake
from string_utils.errors import InvalidInputError

def test_camel_case_to_snake_invalid_input():
    # Test with non-string input, should raise InvalidInputError
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(None)
    
    # Test with a string that is not in camel case format
    assert camel_case_to_snake('notacamelcasestring') == 'notacamelcasestring'

def test_camel_case_to_snake_with_separator():
    # Test with custom separator
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'
    
    # Test with empty separator, should default to underscore
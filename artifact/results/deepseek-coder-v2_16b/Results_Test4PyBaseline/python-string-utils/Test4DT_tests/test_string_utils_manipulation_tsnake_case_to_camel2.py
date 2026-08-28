
# Module: string_utils.manipulation
# test_string_utils.manipulation.py
from string_utils.manipulation import snake_case_to_camel, InvalidInputError

def test_snake_case_to_camel_invalid_input():
    try:
        snake_case_to_camel('invalid-input')
    except InvalidInputError as e:
        assert str(e) == 'invalid-input'

# Test case for handling different separators
def test_snake_case_to_camel_custom_separator():
    assert snake_case_to_camel('foo.bar.baz', separator='.') == 'FooBarBaz'
    assert snake_case_to_camel('foo-bar-baz', separator='-') == 'FooBarBaz'
    assert snake_case_to_camel('foo bar baz', separator=' ') == 'FooBarBaz'  # Assuming this is valid snake case for space as separator

# Test case for non-snake case formats
def test_snake_case_to_camel_non_snake_case():
    assert snake_case_to_camel('CamelCaseIsNotAllowed') == 'CamelCaseIsNotAllowed'  # Non-snake case string
    assert snake_case_to_camel('fooBarBaz') == 'fooBarBaz'  # Already camel case string
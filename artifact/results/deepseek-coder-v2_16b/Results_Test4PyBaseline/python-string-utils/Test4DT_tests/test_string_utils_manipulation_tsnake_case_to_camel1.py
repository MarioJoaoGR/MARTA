
# Module: string_utils.manipulation
from string_utils.manipulation import snake_case_to_camel, InvalidInputError

def test_snake_case_to_camel_invalid_input():
    try:
        snake_case_to_camel('invalid-input')
    except InvalidInputError as e:
        assert str(e) == 'invalid-input'

def test_snake_case_to_camel_default():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'

def test_snake_case_to_camel_no_upper_first():
    assert snake_case_to_camel('foo_bar_baz', upper_case_first=False) == 'fooBarBaz'

def test_snake_case_to_camel_custom_separator():
    assert snake_case_to_camel('foo.bar.baz', separator='.') == 'FooBarBaz'


import pytest
from string_utils.manipulation import snake_case_to_camel

def test_valid_snake_case_default_separator():
    result = snake_case_to_camel('the_snake_is_green')
    assert result == 'TheSnakeIsGreen'

def test_valid_snake_case_custom_separator():
    result = snake_case_to_camel('the-snake-is-green', separator='-')
    assert result == 'TheSnakeIsGreen'


def test_non_string_input():
    with pytest.raises(TypeError):
        snake_case_to_camel(12345, separator='-')

def test_empty_string_input():
    result = snake_case_to_camel('')
    assert result == ''

def test_upper_case_first_false():
    result = snake_case_to_camel('the_snake_is_green', upper_case_first=False)
    assert result == 'theSnakeIsGreen'

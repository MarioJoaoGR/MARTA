
import pytest
from string_utils.manipulation import snake_case_to_camel

def test_default_usage():
    result = snake_case_to_camel('the_snake_is_green')
    assert result == 'TheSnakeIsGreen'


def test_upper_case_first_false():
    result = snake_case_to_camel('the_snake_is_green', upper_case_first=False)
    assert result == 'theSnakeIsGreen'

def test_non_snake_case_input():
    result = snake_case_to_camel('thisIsNotASnakeCaseString')
    assert result == 'thisIsNotASnakeCaseString'
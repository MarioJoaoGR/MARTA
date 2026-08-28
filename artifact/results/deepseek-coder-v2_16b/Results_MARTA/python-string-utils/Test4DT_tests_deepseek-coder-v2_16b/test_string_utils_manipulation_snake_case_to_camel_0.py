
import pytest
from string_utils.manipulation import snake_case_to_camel

def test_snake_case_to_camel_basic():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'


def test_snake_case_to_camel_no_upper_first():
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'

def test_snake_case_to_camel_non_snake_case():
    assert snake_case_to_camel('thisIsNotASnakeCaseString') == 'thisIsNotASnakeCaseString'
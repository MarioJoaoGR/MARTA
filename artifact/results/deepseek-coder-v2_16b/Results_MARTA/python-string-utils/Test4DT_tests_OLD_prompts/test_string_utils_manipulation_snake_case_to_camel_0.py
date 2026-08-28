
import pytest
from string_utils.manipulation import snake_case_to_camel
from string_utils.errors import InvalidInputError
from unittest.mock import patch

# Test for converting a valid snake case to camel case with default settings
def test_valid_snake_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'

# Test for converting a valid snake case to camel case with upper_case_first set to False
def test_valid_snake_to_camel_no_upper():
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'

# Test for converting a valid snake case to camel case with a different separator

# Test for handling non-snake case input strings

# Test for converting an empty string to an empty string (edge case)
def test_empty_string():
    assert snake_case_to_camel('') == ''

# Test for handling None input and expecting it to raise InvalidInputError
def test_none_input():
    with pytest.raises(InvalidInputError):
        snake_case_to_camel(None)
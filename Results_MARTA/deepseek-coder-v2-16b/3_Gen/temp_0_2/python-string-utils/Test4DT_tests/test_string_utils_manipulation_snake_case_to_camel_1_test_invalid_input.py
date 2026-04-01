
import pytest
from unittest.mock import patch
from string_utils.manipulation import snake_case_to_camel

def test_invalid_input():
    with patch('string_utils.manipulation.is_snake_case', return_value=False):
        assert snake_case_to_camel('the_snake_is_green') == 'the_snake_is_green'

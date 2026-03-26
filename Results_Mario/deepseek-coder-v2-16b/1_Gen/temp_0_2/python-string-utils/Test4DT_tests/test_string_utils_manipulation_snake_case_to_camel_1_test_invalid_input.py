
import pytest
from string_utils.manipulation import snake_case_to_camel

def test_invalid_input():
    # Test case where the input is not a valid snake case string
    assert snake_case_to_camel('invalid-input') == 'invalid-input'

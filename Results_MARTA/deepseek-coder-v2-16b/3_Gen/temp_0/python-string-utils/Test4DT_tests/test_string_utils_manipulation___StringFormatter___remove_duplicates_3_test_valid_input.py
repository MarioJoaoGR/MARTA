
# Assuming the following structure and imports in string_utils/manipulation/__init__.py
# from .string_formatter import __StringFormatter  # This should be imported correctly
# from ..errors import InvalidInputError  # Similarly, this should be imported correctly

import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

def test_valid_input():
    input_string = "valid string"
    formatter = __StringFormatter(input_string)
    assert formatter.input_string == input_string

def test_invalid_input():
    invalid_input = 12345
    with pytest.raises(InvalidInputError):
        __StringFormatter(invalid_input)

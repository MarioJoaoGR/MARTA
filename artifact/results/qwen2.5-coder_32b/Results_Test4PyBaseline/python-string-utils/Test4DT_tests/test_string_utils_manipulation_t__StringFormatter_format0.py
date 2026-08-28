
# Test case  
import pytest
import re  # Importing the re module to resolve the undefined variable error
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_string_formatter_initialization_with_valid_string():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

def test_string_formatter_initialization_with_invalid_type():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_format_basic_string():
    formatter = __StringFormatter("hello   world! This is a test.")
    formatted_string = formatter.format()
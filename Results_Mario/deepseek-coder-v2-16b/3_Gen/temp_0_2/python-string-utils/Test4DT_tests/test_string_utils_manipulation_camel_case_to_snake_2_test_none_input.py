
import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def test_none_input():
    # Test when input is None
    with pytest.raises(InvalidInputError):
        assert camel_case_to_snake(None) == None

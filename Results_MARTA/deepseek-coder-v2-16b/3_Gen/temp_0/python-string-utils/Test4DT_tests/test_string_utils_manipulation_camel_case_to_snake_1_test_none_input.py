
import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def test_none_input():
    # Test case for None input
    with pytest.raises(InvalidInputError):
        result = camel_case_to_snake(None)

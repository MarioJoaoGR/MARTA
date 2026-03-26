
import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def test_none_input():
    # Test handling of None input
    with pytest.raises(InvalidInputError):
        assert camel_case_to_snake(None) is None

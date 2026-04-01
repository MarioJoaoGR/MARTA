
import pytest
from string_utils.errors import InvalidInputError
from string_utils.manipulation import booleanize

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        booleanize(None)  # Example of an invalid input
        booleanize('')    # Another example of an invalid input

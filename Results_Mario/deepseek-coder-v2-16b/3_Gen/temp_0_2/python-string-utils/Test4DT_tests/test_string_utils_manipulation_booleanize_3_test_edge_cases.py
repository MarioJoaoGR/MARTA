
import pytest
from string_utils.manipulation import booleanize

def is_string(input_str):
    return isinstance(input_str, str)

class InvalidInputError(Exception):
    pass

@pytest.mark.parametrize("input_string, expected", [
    ("true", True),
    ("True", True),
    ("TRUE", True),
    ("1", True),
    ("yes", True),
    ("Yes", True),
    ("YES", True),
    ("y", True),
    ("Y", True),
    ("nope", False),
    ("NOPE", False),
    ("no", False),
    ("No", False),
    ("nono", False),
])
def test_booleanize(input_string, expected):
    if not is_string(input_string):
        with pytest.raises(InvalidInputError):
            booleanize(input_string)
    else:
        assert booleanize(input_string) == expected

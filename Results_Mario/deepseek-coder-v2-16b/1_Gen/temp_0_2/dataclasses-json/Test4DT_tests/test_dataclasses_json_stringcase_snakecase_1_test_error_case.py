
import re
from unittest.mock import patch
import pytest

def snakecase(string):
    """Convert string into snake case.
    Join punctuation with underscore

    Args:
        string: String to convert.

    Returns:
        string: Snake cased string.

    """

    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    
    string = re.sub(r"[\-\.\s]", '_', str(string))
    if not string:
        return string
    return (uplowcase(string[0], 'low')
            + re.sub(r"[A-Z0-9]",
                     lambda matched: '_' + uplowcase(matched.group(0), 'low'),
                     string[1:]))

def uplowcase(char, case):
    if case == 'low':
        return char.lower()
    else:
        return char.upper()

@pytest.mark.parametrize("input_string", [None, 123, [], {}])
def test_error_case(input_string):
    with pytest.raises(ValueError):
        snakecase(input_string)

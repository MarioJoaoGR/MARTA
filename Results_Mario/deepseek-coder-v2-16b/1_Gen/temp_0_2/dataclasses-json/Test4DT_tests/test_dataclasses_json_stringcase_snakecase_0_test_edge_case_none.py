
import re
from unittest.mock import patch

def snakecase(string):
    """Convert string into snake case.
    Join punctuation with underscore

    Args:
        string: String to convert.

    Returns:
        string: Snake cased string.

    """

    if string is None:
        return None
    
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

import pytest

@pytest.mark.parametrize("input_string", [None])
def test_edge_case_none(input_string):
    assert snakecase(input_string) is None


import re

def uplowcase(char, case):
    """Helper function to convert character case."""
    if case == 'low':
        return char.lower()
    elif case == 'up':
        return char.upper()
    else:
        raise ValueError("Invalid case specified")

def snakecase(string):
    """Convert string into snake case. Join punctuation with underscore."""
    if string is None:
        return ''
    string = re.sub(r"[\-\.\s]", '_', str(string))
    if not string:
        return string
    return (uplowcase(string[0], 'low')
            + re.sub(r"[A-Z0-9]",
                     lambda matched: '_' + uplowcase(matched.group(0), 'low'),
                     string[1:]))

# Test for handling None input
def test_edge_case_none():
    assert snakecase(None) == ''

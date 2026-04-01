
import pytest

def uplowcase(string, case):
    """Convert string into upper or lower case.

    Args:
        string: String to convert.

    Returns:
        string: Uppercase or lowercase case string.

    """
    if case == 'up':
        return str(string).upper()
    elif case == 'low':
        return str(string).lower()

def test_valid_lowcase():
    assert uplowcase("Python Programming", "low") == "python programming"


import pytest

def is_comment(line: str | None) -> bool:
    """
    Determines whether a given string represents a comment based on the presence of a '#' character at the beginning.
    
    Parameters:
        line (str | None): The string to be checked for a comment. If `None`, the function will return False.
        
    Returns:
        bool: True if the input string starts with '#', otherwise False.
        
    Examples:
        >>> is_comment(" # This is a comment")  # True, because it starts with '#'
        >>> is_comment("This is not a comment")  # False, because it does not start with '#'
        >>> is_comment(None)  # False, because the input is None
        >>> is_comment("")  # False, because an empty string does not start with '#'
    """
    return line.startswith("#") if line else False

def test_none_input():
    assert not is_comment(None), "Expected False for None input"

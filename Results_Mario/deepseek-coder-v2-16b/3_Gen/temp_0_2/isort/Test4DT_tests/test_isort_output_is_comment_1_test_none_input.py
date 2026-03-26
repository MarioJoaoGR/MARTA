
import pytest

def is_comment(line: str | None) -> bool:
    """
    Determines whether a given string represents a comment based on the presence of a '#' character at the beginning.
    
    Parameters:
        line (str | None): The input string to be checked for a comment. If `None`, the function returns False.
        
    Returns:
        bool: True if the input string starts with '#', otherwise False.
        
    Examples:
        >>> is_comment("This is a comment # This is not visible")
        True
        
        >>> is_comment("This is not a comment")
        False
        
        >>> is_comment(None)
        False
        
        >>> is_comment("# This is a hidden comment")
        True
    """
    return line.startswith("#") if line else False

def test_none_input():
    assert not is_comment(None)


import pytest
import typing as T

def _clean_str(string: str) -> T.Optional[str]:
    """
    Cleans a given string by stripping leading and trailing whitespace characters, and returns the cleaned string if it is not empty; otherwise, it returns `None`.

    Parameters:
        string (str): The input string that needs to be cleaned.

    Returns:
        Optional[str]: The cleaned string if the input string is not empty, otherwise None.

    Examples:
        >>> _clean_str("  Hello, World!  ")
        'Hello, World!'
        
        >>> _clean_str("")
        None
        
        >>> _clean_str("   ")
        None
    """
    string = string.strip()
    if len(string) > 0:
        return string
    return None

def test_valid_input():
    assert _clean_str("  Hello, World!  ") == 'Hello, World!'
    assert _clean_str("") is None
    assert _clean_str("   ") is None

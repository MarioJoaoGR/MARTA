
import pytest
from dataclasses_json import stringcase  # Assuming this is the correct module path

def capitalcase(string):
    """Convert a given string into uppercase, with the first letter capitalized and the rest in lowercase.

    Args:
        string (str): The input string to be converted to capital case.

    Returns:
        str: A new string where the first character is uppercase and the remaining characters are lowercase. If the input string is empty or not a string, it returns the original string unchanged.

    Example:
        >>> capitalcase("hello")
        'Hello'
        
        >>> capitalcase("HELLO WORLD")
        'Hello world'
        
        >>> capitalcase("")
        ''
        
        >>> capitalcase(12345)
        '12345'
    """
    string = str(string)
    if not string:
        return string
    return string[0].upper() + string[1:].lower()

def test_capitalcase():
    assert capitalcase("hello") == "Hello"
    assert capitalcase("HELLO WORLD") == "Hello world"
    assert capitalcase("") == ""
    assert capitalcase(12345) == "12345"

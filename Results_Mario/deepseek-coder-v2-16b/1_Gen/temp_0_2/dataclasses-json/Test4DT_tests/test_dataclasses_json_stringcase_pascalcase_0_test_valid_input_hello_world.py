
import pytest
from dataclasses_json.stringcase import camelcase, capitalcase

def pascalcase(string):
    """Convert a given string into PascalCase. The function first converts the input string to camel case using the `camelcase` function, and then capitalizes the first letter of each word in the camel case string.

    Args:
        string (str): The input string to be converted to PascalCase.

    Returns:
        str: A PascalCase formatted string.

    Examples:
        >>> pascalcase("hello_world")
        'HelloWorld'
        
        >>> pascalcase("PYTHON programming")
        'PythonProgramming'
        
        >>> pascalcase("123abc def")
        '123AbcDef'
        
        >>> pascalcase("-START-MIDDLE-END-")
        'StartMiddleEnd'
    """
    return capitalcase(camelcase(string))

def test_valid_input_hello_world():
    assert pascalcase("hello_world") == "HelloWorld"

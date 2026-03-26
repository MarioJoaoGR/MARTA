
import re
from dataclasses_json import stringcase

def spinalcase(string):
    """Convert a given string into spinal case by joining punctuation with hyphens.
    
    This function first converts the input string to snake case by replacing hyphens, dots, and spaces with underscores. Then it replaces all underscores with hyphens to produce a spinal cased string.

    Args:
        string (str): The input string to be converted into spinal case.

    Returns:
        str: The spinal cased version of the input string.

    Examples:
        >>> spinalcase("Hello-World")
        'hello-world'
        
        >>> spinalcase("Python Programming Language")
        'python-programming-language'
        
        >>> spinalcase("123 Number Example")
        '123-number-example'
        
        >>> spinalcase("")
        ''
    """
    return re.sub(r"_", "-", stringcase.snakecase(string))

import pytest

def test_edge_case_empty_string():
    assert spinalcase("") == ""

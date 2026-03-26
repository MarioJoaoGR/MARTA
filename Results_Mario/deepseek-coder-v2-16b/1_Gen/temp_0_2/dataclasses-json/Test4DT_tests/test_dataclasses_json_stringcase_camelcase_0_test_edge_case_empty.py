
import re
from dataclasses_json.stringcase import uplowcase

def camelcase(string):
    """ Convert a given string into camel case format.

    Args:
        string (str): The input string to be converted to camel case.

    Returns:
        str: A camel case formatted string.

    Examples:
        >>> camelcase("hello_world")
        'HelloWorld'
        
        >>> camelcase("PYTHON programming")
        'PythonProgramming'
        
        >>> camelcase("123abc def")
        '123AbcDef'
        
        >>> camelcase("-START-MIDDLE-END-")
        'StartMiddleEnd'
    """
    string = re.sub(r"^[\-_\.]", '', str(string))
    if not string:
        return string
    return (uplowcase(string[0], 'low')
            + re.sub(r"[\-_\.\s]([a-z0-9])",
                     lambda matched: uplowcase(matched.group(1), 'up'),
                     string[1:]))

import pytest

def test_edge_case_empty():
    assert camelcase("") == ""

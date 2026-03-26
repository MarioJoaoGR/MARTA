
import pytest
from docstring_parser.tests.test_epydoc import parse, compose

def test_short_rtype() -> None:
    """Test abbreviated docstring with only return type information.

    This function constructs and parses an epydoc-style docstring that includes a short description followed by a return type specification. It then asserts that the parsed result matches the original string, ensuring consistency in parsing and formatting of such docstrings.

    Examples:
        >>> test_short_rtype()
        This will run the function and assert that the parsed docstring matches the expected format with only a return type specified.

    What it is intended to do:
    Tests the parsing of a short docstring containing only return type information.

    This function constructs and parses a test docstring with a short description followed by an RTYPEDOC tag, 
    asserting that the parsed result matches the original string format. It is designed to verify the functionality 
    of the docstring parser in handling basic documentation formats, particularly focusing on return type annotations.

    Parameters:
        None

    Returns:
        None
"""
    string = "Short description.\n\n@rtype: float"
    docstring = parse(string)
    assert compose(docstring) == string

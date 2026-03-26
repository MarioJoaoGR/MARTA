# Module: docstring_parser.tests.test_epydoc
# Import the function from its module
from docstring_parser import parse, compose
import pytest

def test_short_rtype():
    """Test abbreviated docstring with only return type information."""
    # Define the input string containing the abbreviated docstring
    string = "Short description.\n\n@rtype: float"
    
    # Parse the docstring and store the result in a variable
    parsed_docstring = parse(string)
    
    # Assert that the composed version of the parsed docstring matches the original input string
    assert compose(parsed_docstring) == string

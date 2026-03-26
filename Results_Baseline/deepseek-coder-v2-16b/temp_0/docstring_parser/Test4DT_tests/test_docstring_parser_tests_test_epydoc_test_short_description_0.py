
# Module: docstring_parser.tests.test_epydoc
# Import the function to be tested
from docstring_parser import parse
import typing as T

def test_short_description():
    # Test case 1: Source code with a valid short description
    source = """
    Example function to demonstrate parsing.
    @param arg1: The first argument
    @return: The result of the operation
    """
    expected = "Example function to demonstrate parsing."
    docstring = parse(source)
    assert docstring.short_description == expected, f"Expected short description '{expected}', but got '{docstring.short_description}'"
    assert docstring.long_description is None, "Expected long description to be None"

import pytest
from docstring_parser.tests.test_google import test_compose, parse, compose

def test_valid_input():
    source = "This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer."
    expected_composition = """This is a summary.

Args:
    param1 (int): Description of parameter 1.
    param2 (str): Description of parameter 2.

Returns:
    int: The result of the operation, which could be an integer."""
    
    assert compose(parse(source)) == expected_composition

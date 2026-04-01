
import pytest
from docstring_parser.tests.test_epydoc import parse, test_returns

def test_valid_input_with_specified_return_type():
    # Test case 1: No return specified
    docstring = parse("Short description")
    assert docstring.returns is None

    # Test case 2: Return with no type specified
    docstring = parse("Short description\n@return: description")
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator

    # Test case 3: Return with type specified
    docstring = parse("Short description\n@return: description\n@rtype: int")
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator


import pytest
from docstring_parser.tests.test_epydoc import parse

def test_valid_input_happy_path():
    """Test standard input with valid docstrings containing yield annotations."""
    # Test case 1: No return statement in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    # Test case 2: Single yield without type annotation
    docstring = parse(
        """
        Short description
        @yield: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator

    # Test case 3: Single yield with type annotation
    docstring = parse(
        """
        Short description
        @yield: description
        @ytype: int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator

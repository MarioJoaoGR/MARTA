
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_valid_input_no_yield():
    """Test when docstring contains no yield annotation."""
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

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

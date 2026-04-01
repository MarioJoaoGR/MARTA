
import pytest
from docstring_parser.tests.test_epydoc import parse, test_returns

def test_valid_input_no_return():
    """Test parsing a docstring with no return value specified."""
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    docstring = parse(
        """
        Short description
        @return: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator

    docstring = parse(
        """
        Short description
        @return: description
        @rtype: int
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert not docstring.returns.is_generator

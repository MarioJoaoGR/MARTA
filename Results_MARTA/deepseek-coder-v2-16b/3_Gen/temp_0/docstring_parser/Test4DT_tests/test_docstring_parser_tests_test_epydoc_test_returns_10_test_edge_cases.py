
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_returns() -> None:
    """Test parsing returns."""
    # Test case for no return type specified
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    # Test case for return type with only a description
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

    # Test case for return type with both description and specified type
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

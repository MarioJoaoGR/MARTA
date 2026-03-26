
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_returns() -> None:
    """Test parsing returns."""
    # Test case for no return statement
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    # Test case for return with no type specification
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

    # Test case for return with type specification
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

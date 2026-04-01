
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_yields() -> None:
    """Test parsing yields."""
    # Test no yield in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    # Test single yield without type annotation
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

    # Test single yield with type annotation
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

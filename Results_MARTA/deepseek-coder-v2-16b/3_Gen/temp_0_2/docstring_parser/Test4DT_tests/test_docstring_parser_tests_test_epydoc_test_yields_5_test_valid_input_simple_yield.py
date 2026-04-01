
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_yields() -> None:
    """Test parsing yields."""
    # Test case for no yield in the docstring
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None

    # Test case for a single yield without type annotation
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

    # Test case for a single yield with type annotation
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

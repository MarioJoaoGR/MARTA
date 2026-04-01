
import pytest
from docstring_parser.tests.test_rest import parse

def test_yields() -> None:
    """Test parsing yields."""
    # Test case 1: No yield statements
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

    # Test case 2: Single yield statement without type specification
    docstring = parse(
        """
        Short description
        :yields: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name is None
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

    # Test case 3: Single yield statement with type specification
    docstring = parse(
        """
        Short description
        :yields int: description
        """
    )
    assert docstring.returns is not None
    assert docstring.returns.type_name == "int"
    assert docstring.returns.description == "description"
    assert docstring.returns.is_generator
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 1
    assert docstring.many_returns[0] == docstring.returns

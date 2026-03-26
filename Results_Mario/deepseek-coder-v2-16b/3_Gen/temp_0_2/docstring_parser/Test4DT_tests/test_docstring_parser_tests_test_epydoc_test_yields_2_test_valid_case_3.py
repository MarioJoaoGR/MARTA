
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_valid_case_3():
    """Test parsing a docstring with multiple yield annotations including types."""
    # Test case 1: No yield annotation
    docstring = parse('Short description')
    assert docstring.returns is None

    # Test case 2: Single yield without type
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

    # Test case 3: Multiple yields with explicit type
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

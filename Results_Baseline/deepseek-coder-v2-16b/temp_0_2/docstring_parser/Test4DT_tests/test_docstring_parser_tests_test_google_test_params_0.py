
import pytest
from docstring_parser import parse, DocstringParam  # Corrected import path

def test_parse_empty_docstring():
    """Test parsing a docstring with no parameters."""
    docstring = parse("Short description")
    assert len(docstring.params) == 0

def test_parse_single_param():
    """Test parsing a docstring with a single parameter."""
    docstring = parse(
        """
        Short description

        Args:
            name: description 1
        """
    )
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description 1"
    assert not docstring.params[0].is_optional

def test_parse_multiple_params():
    """Test parsing a docstring with multiple parameters."""
    docstring = parse(
        """
        Short description

        Args:
            name: description 1
            priority (int): description 2
            sender (str?): description 3
            ratio (Optional[float], optional): description 4
        """
    )
    assert len(docstring.params) == 4
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description 1"
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional
    assert docstring.params[2].arg_name == "sender"
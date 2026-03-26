
import pytest
from docstring_parser import parse

def test_parse_empty_docstring():
    """Test parsing an empty docstring."""
    docstring = parse("")
    assert len(docstring.params) == 0

def test_parse_single_param():
    """Test parsing a single parameter in the docstring."""
    docstring = parse("Short description\n:param name: description of name")
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description of name"
    assert docstring.params[0].default is None
    assert not docstring.params[0].is_optional

def test_parse_multiple_params():
    """Test parsing multiple parameters in the docstring."""
    docstring = parse(
        """
        Short description

        :param name: description of name
        :param age: description of age
        :param city: description of city
        """
    )
    assert len(docstring.params) == 3
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description of name"
    assert docstring.params[0].default is None
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "age"
    assert docstring.params[1].type_name is None
    assert docstring.params[1].description == "description of age"
    assert docstring.params[1].default is None
    assert not docstring.params[1].is_optional
    assert docstring.params[2].arg_name == "city"
    assert docstring.params[2].type_name is None
    assert docstring.params[2].description == "description of city"
    assert docstring.params[2].default is None
    assert not docstring.params[2].is_optional

def test_parse_param_with_multiline_default():
    """Test parsing a parameter with a multiline default value specified in the docstring."""
    docstring = parse(
        """
        Short description

        :param name: description of name
        :param message: description of message, defaults to 'hello'
        """
    )
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description of name"
    assert docstring.params[0].default is None
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "message"
    assert docstring.params[1].type_name is None
    assert docstring.params[1].description == "description of message, defaults to 'hello'"
    assert docstring.params[1].default == "'hello'"
    assert not docstring.params[1].is_optional

def test_parse_docstring_with_no_params():
    """Test parsing a docstring with no parameters."""
    docstring = parse("Short description")
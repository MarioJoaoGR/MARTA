
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_valid_input_basic_docstring():
    """Test parsing a basic docstring with no raise statements."""
    docstring = parse(
        """
        Short description
        """
    )
    assert len(docstring.raises) == 0

    docstring = parse(
        """
        Short description
        @raise: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name is None
    assert docstring.raises[0].description == "description"

    docstring = parse(
        """
        Short description
        @raise ValueError: description
        """
    )
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"

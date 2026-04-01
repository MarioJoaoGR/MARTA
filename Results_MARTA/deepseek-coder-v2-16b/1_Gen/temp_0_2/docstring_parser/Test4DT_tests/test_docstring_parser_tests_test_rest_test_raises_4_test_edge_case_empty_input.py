
import pytest
from docstring_parser.tests.test_rest import parse

def test_raises() -> None:
    """Test parsing raises."""
    docstring = parse('')
    assert len(docstring.raises) == 0

    docstring = parse(':raises: description')
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name is None
    assert docstring.raises[0].description == "description"

    docstring = parse(':raises ValueError: description')
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == "ValueError"
    assert docstring.raises[0].description == "description"

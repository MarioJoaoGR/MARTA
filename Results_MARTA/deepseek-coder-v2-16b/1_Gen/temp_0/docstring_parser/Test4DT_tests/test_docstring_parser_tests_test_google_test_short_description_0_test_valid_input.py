
import pytest
from docstring_parser.tests.test_google import parse, test_short_description

def test_valid_input():
    """Test parsing short description."""
    source = "This is a summary."
    expected = "This is a summary."
    
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta


import pytest
from docstring_parser.tests.test_rest import parse, compose, RenderingStyle

def test_valid_input():
    """Test standard input with valid docstring containing only return type information."""
    string = "Short description.\n\n:rtype: float"
    docstring = parse(string)
    rendering_style = RenderingStyle.EXPANDED
    assert compose(docstring, rendering_style=rendering_style) == string

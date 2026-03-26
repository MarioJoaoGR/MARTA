
import pytest
from docstring_parser.tests.test_rest import parse, compose, RenderingStyle

def test_short_rtype() -> None:
    """Test abbreviated docstring with only return type information."""
    string = "Short description.\n\n:rtype: float"
    docstring = parse(string)
    rendering_style = RenderingStyle.EXPANDED
    assert compose(docstring, rendering_style=rendering_style) == string


from docstring_parser.tests.test_epydoc import parse, compose

def test_short_rtype() -> None:
    """Test abbreviated docstring with only return type information."""
    string = "Short description.\n\n@rtype: float"
    docstring = parse(string)
    assert compose(docstring) == string

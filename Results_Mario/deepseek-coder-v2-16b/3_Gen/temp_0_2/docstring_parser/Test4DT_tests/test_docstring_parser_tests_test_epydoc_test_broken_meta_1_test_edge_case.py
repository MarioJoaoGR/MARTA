
import pytest
from docstring_parser.tests.test_epydoc import parse, ParseError

def test_broken_meta() -> None:
    """Test parsing broken meta."""
    with pytest.raises(ParseError):
        parse("@")

    with pytest.raises(ParseError):
        parse("@param herp derp")

    with pytest.raises(ParseError):
        parse("@param: invalid")

    with pytest.raises(ParseError):
        parse("@param with too many args: desc")

    # these should not raise any errors
    parse("@sthstrange: desc")

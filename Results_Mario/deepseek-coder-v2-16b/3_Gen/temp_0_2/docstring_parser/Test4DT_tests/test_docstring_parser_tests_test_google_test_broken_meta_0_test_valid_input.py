
import pytest
from docstring_parser.tests.test_google import parse, ParseError

def test_broken_meta() -> None:
    """Test parsing broken meta."""
    with pytest.raises(ParseError):
        parse("Args:")

    with pytest.raises(ParseError):
        parse("Args:\n\n")

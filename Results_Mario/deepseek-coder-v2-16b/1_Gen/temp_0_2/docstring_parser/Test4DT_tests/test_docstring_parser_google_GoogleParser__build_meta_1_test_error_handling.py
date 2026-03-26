
import pytest
from docstring_parser.google import GoogleParser, ParseError

def test_error_handling():
    parser = GoogleParser()
    with pytest.raises(ParseError) as exc_info:
        parser._build_meta('NoColonHere', 'Parameters')
    assert str(exc_info.value) == "Expected a colon in 'NoColonHere'."

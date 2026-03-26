
import pytest
from docstring_parser.google import GoogleParser, Section, ParseError

def test_invalid_input():
    parser = GoogleParser(sections=[Section('Args', [], 'Arguments for the function.')], title_colon=False)
    with pytest.raises(ParseError):
        parser._build_meta('text without colon', 'Args')

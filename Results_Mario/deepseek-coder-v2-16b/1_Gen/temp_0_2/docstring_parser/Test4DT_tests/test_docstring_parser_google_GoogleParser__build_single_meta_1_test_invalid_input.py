
import pytest
from docstring_parser.google import GoogleParser, ParseError

def test_invalid_input():
    try:
        parser = GoogleParser(sections=['InvalidSection'], title_colon=True)
    except ParseError as e:
        assert str(e) == "Unknown section type 'InvalidSection'"


import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS, Docstring, DocstringStyle, ParseError, SectionType
import typing as T

@pytest.fixture
def parser():
    return GoogleParser()

def test_parse_none(parser):
    """Test handling of None input."""
    assert parser.parse(None) is not None  # Ensure it returns a Docstring object even if the input is None
    assert parser.parse("") is not None  # Ensure it returns a Docstring object for an empty string

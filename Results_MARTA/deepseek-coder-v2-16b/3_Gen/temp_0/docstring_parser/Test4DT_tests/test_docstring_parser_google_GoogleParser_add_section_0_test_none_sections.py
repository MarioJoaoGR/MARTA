
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_none_sections():
    parser = GoogleParser(sections=None, title_colon=True)
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is True

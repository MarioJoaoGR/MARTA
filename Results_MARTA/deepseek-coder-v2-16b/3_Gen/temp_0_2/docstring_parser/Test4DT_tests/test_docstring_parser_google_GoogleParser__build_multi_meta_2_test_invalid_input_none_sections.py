
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_invalid_input_none_sections():
    parser = GoogleParser(sections=None)
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}

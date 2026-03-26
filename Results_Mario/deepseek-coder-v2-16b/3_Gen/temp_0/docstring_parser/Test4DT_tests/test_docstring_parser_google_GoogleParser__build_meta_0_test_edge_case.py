
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS, ParseError, SectionType

@pytest.fixture
def parser():
    return GoogleParser()

def test_edge_case(parser):
    # Test edge case where no sections are provided and default sections should be used
    parser = GoogleParser(sections=None, title_colon=True)
    
    assert parser.title_colon is True
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
    for section in DEFAULT_SECTIONS:
        assert section.title in parser.sections

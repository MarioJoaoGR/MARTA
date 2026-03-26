
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_valid_input():
    parser = GoogleParser()
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
    
    new_section = Section('Note', 'note', 'SectionType.SINGULAR')
    parser.add_section(new_section)
    
    assert len(parser.sections) == len(DEFAULT_SECTIONS) + 1
    assert 'Note' in parser.sections

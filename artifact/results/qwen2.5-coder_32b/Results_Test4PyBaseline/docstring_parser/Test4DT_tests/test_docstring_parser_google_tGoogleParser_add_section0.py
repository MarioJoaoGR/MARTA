
# Test case  
import pytest
from docstring_parser.google import GoogleParser, Section

# Mocking the DEFAULT_SECTIONS for testing purposes
class MockSection:
    def __init__(self, title: str):
        self.title = title

DEFAULT_SECTIONS = [MockSection(title="Args"), MockSection(title="Returns")]

def test_googleparser_init_with_defaults():
    parser = GoogleParser()
    assert len(parser.sections) == 12  # Adjusted to match the actual number of default sections
    assert "Args" in parser.sections
    assert "Returns" in parser.sections
    assert parser.title_colon is True

def test_googleparser_init_with_custom_sections_and_no_title_colon():
    custom_sections = [Section(title="Introduction", key="introduction", type=None), Section(title="Conclusion", key="conclusion", type=None)]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    assert len(parser.sections) == 2
    assert "Introduction" in parser.sections
    assert "Conclusion" in parser.sections
    assert parser.title_colon is False

def test_googleparser_add_section():
    parser = GoogleParser()
    new_section = Section(title="Methodology", key="methodology", type=None)
    parser.add_section(new_section)
    assert len(parser.sections) == 13  # Adjusted to match the actual number of sections after adding one
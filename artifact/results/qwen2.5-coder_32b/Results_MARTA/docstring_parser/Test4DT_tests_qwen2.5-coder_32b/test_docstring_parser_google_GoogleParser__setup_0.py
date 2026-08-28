
import pytest
from docstring_parser.google import GoogleParser, Section, SectionType

def test_googleparser_with_default_sections_and_colons():
    parser = GoogleParser()
    assert len(parser.sections) > 0  # Ensure default sections are set up
    assert parser.title_colon is True  # Ensure colons are expected after section titles

def test_googleparser_with_custom_sections_no_colons():
    custom_sections = [
        Section(title="Introduction", key="introduction", type=SectionType.SINGULAR),
        Section(title="Conclusion", key="conclusion", type=SectionType.SINGULAR)
    ]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    assert len(parser.sections) == 2
    assert parser.title_colon is False

def test_googleparser_with_default_sections_no_colons():
    parser = GoogleParser(title_colon=False)
    assert len(parser.sections) > 0  # Ensure default sections are set up
    assert parser.title_colon is False  # Ensure no colons are expected after section titles

def test_googleparser_with_custom_sections_and_colons():
    custom_sections = [
        Section(title="Methodology", key="methodology", type=SectionType.SINGULAR),
        Section(title="Results", key="results", type=SectionType.MULTIPLE)
    ]
    parser = GoogleParser(sections=custom_sections, title_colon=True)
    assert len(parser.sections) == 2
    assert parser.title_colon is True

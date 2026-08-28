
import pytest
from docstring_parser.google import GoogleParser, Section, SectionType

def test_add_section_none_title():
    parser = GoogleParser()
    new_section_none_title = Section(title=None, key="methodology", type=SectionType.SINGULAR)
    
    # Attempt to add a section with None title
    parser.add_section(new_section_none_title)
    
    # Since the title is None, it should not be added as a key in the sections dictionary
    assert "None" not in parser.sections


def test_add_section_valid_title():
    parser = GoogleParser()
    new_section_valid_title = Section(title="Methodology", key="methodology", type=SectionType.SINGULAR)
    
    # Attempt to add a valid section
    parser.add_section(new_section_valid_title)
    
    # The title should be added as a key in the sections dictionary
    assert "Methodology" in parser.sections

def test_add_section_existing_title():
    parser = GoogleParser()
    new_section_initial = Section(title="Arguments", key="param", type=SectionType.MULTIPLE)
    new_section_modified = Section(title="Arguments", key="modified_param", type=SectionType.SINGULAR)
    
    # Initially add a section
    parser.add_section(new_section_initial)
    # Replace the section with a new one having the same title
    parser.add_section(new_section_modified)
    
    # The section should be replaced with the new one
    assert parser.sections["Arguments"].key == "modified_param"
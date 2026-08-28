
import pytest
from docstring_parser.numpydoc import Section

def test_section_initialization():
    section = Section("Parameters", "param")
    assert section.title == "Parameters"
    assert section.key == "param"

def test_section_title_pattern():
    section = Section("Parameters", "param")
    expected_pattern = r"^(Parameters)\s*?\n------------\s*$"
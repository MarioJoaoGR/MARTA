
import pytest
from docstring_parser.numpydoc import Section

# Test initialization of Section class
def test_section_initialization():
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
    assert section.key == "params"

# Test title pattern generation
def test_title_pattern():
    section = Section(title="Parameters", key="params")
    expected_pattern = r"^Parameters\s*?\n----------"
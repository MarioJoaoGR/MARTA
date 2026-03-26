
import pytest
from docstring_parser.numpydoc import Section

def test_section_initialization():
    """Test that a Section object can be initialized with a title and key."""
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
    assert section.key == "params"

def test_section_str_representation():
    """Test the string representation of a Section object."""
    section = Section(title="Parameters", key="params")
    expected_str = f"Section(title='{section.title}', key='{section.key}')"
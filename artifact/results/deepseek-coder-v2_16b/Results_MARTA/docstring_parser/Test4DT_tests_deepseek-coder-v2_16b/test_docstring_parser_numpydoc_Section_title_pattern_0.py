
import pytest
from docstring_parser.numpydoc import Section

def test_valid_section():
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
    assert section.key == "params"

def test_invalid_type_creation():
    with pytest.raises(TypeError):
        section = Section()  # This should raise a TypeError because the required arguments are not provided


import pytest
from docstring_parser.numpydoc import Section

def test_valid_init():
    """Test that a valid Section object can be initialized."""
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
    assert section.key == "params"

def test_invalid_input():
    """Test that an invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        Section()  # No arguments provided, should raise TypeError

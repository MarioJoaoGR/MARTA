
import pytest
from docstring_parser.numpydoc import Section

def test_valid_init():
    """Test that a valid instance of Section can be created."""
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
    assert section.key == "params"

def test_invalid_input():
    """Test that an invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        Section()  # Attempt to create without arguments should raise TypeError

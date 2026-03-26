
import pytest
from docstring_parser.numpydoc import Section

def test_valid_inputs():
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
    assert section.key == "params"

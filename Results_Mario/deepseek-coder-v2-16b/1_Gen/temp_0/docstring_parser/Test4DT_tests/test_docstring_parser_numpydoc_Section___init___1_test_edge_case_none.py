
import pytest
from docstring_parser.numpydoc import Section

def test_edge_case_none():
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
    assert section.key == "params"


import pytest
from docstring_parser.numpydoc import Section

def test_edge_case_none():
    section = Section(title=None, key=None)
    assert section.title is None
    assert section.key is None

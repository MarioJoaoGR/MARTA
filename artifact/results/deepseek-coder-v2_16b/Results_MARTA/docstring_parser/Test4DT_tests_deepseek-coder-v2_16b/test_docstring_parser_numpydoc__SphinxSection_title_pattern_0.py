
import pytest
from docstring_parser.numpydoc import Section

def test_valid_input():
    sphinx_section = Section(title="Parameters", key="params")
    assert hasattr(sphinx_section, 'title') and sphinx_section.title == "Parameters"
    assert hasattr(sphinx_section, 'key') and sphinx_section.key == "params"

def test_edge_case_none():
    with pytest.raises(TypeError):
        sphinx_section = Section()

def test_invalid_input():
    with pytest.raises(TypeError):
        sphinx_section = Section()


from docstring_parser.numpydoc import Section

def test_valid_input():
    section = Section(title="Parameters", key="params")
    assert section.title == "Parameters"
    assert section.key == "params"

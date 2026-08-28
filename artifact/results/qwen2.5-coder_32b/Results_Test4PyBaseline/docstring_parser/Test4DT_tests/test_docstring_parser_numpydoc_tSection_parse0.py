
import pytest
from docstring_parser.numpydoc import Section, DocstringMeta

def test_section_initialization():
    section = Section("Parameters", "param")
    assert section.title == "Parameters"
    assert section.key == "param"

def test_section_parse_single_line():
    section = Section("Parameters", "param")
    text = """
        arg1: Description of arg1.
    """
    parsed = list(section.parse(text))
    assert len(parsed) == 1
    assert isinstance(parsed[0], DocstringMeta)
    assert parsed[0].args == ["param"]
    assert parsed[0].description == "arg1: Description of arg1."

def test_section_parse_multiple_lines():
    section = Section("Parameters", "param")
    text = """
        arg1: Description of arg1.
        arg2: Description of arg2.
    """
    parsed = list(section.parse(text))
    assert len(parsed) == 1
    assert isinstance(parsed[0], DocstringMeta)
    assert parsed[0].args == ["param"]
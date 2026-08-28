
import pytest
from docstring_parser.google import GoogleParser, Section, DocstringReturns

def test_build_single_meta_returns():
    parser = GoogleParser()
    section = Section(title="Returns", key="returns", type="return_section")
    desc = "The sum of two numbers"
    meta = parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringReturns)
    assert meta.description == desc

def test_build_single_meta_raises():
    parser = GoogleParser()
    section = Section(title="Raises", key="raises", type="raise_section")
    desc = "If the input is out of range"
    meta = parser._build_single_meta(section, desc)
    assert meta.args == ["raises"]
    assert meta.description == desc

def test_build_single_meta_note():
    parser = GoogleParser()
    section = Section(title="Note", key="note", type="note_section")
    desc = "This function may take a while to execute."
    meta = parser._build_single_meta(section, desc)
    assert meta.args == ["note"]
    assert meta.description == desc

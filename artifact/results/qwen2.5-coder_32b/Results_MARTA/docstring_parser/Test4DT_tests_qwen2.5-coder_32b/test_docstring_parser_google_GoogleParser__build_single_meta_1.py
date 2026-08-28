
import pytest
from docstring_parser.google import GoogleParser, Section, DocstringReturns, DocstringRaises, DocstringMeta

def test_build_single_meta_returns():
    parser = GoogleParser()
    section = Section(title="Returns", key="returns", type="return_type")
    desc = "The sum of two numbers"
    meta = parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringReturns)
    assert meta.description == desc

def test_build_single_meta_raises():
    parser = GoogleParser()
    section = Section(title="Raises", key="raises", type="exception_type")
    desc = "If the input is out of range"
    meta = parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringRaises)
    assert meta.description == desc

def test_build_single_meta_generic():
    parser = GoogleParser()
    section = Section(title="Note", key="note", type="generic_type")
    desc = "This function may take a while to execute."
    meta = parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringMeta)
    assert meta.description == desc

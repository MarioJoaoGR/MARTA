
import pytest
from docstring_parser.google import GoogleParser, Section, DocstringMeta, DocstringRaises

def test_build_single_meta_raises():
    parser = GoogleParser()
    section = Section(key='raises', title='Raises', type=None)
    desc = 'If the input is out of range'
    meta = parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringRaises)

def test_build_single_meta_note():
    parser = GoogleParser()
    section = Section(key='note', title='Note', type=None)
    desc = 'This function may take a while to execute.'
    meta = parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringMeta)

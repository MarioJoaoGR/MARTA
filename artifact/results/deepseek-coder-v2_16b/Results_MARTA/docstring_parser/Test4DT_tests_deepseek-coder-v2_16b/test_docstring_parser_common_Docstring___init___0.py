
import pytest
from docstring_parser.common import Docstring, DocstringMeta

def test_valid_init():
    doc = Docstring()
    assert isinstance(doc, Docstring)
    assert doc.short_description is None
    assert doc.long_description is None
    assert not doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert len(doc.meta) == 0

def test_missing_attributes():
    doc = Docstring()
    assert isinstance(doc, Docstring)
    assert doc.short_description is None
    assert doc.long_description is None
    assert not doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert len(doc.meta) == 0

def test_invalid_init():
    with pytest.raises(TypeError):
        doc = Docstring('invalid_input')

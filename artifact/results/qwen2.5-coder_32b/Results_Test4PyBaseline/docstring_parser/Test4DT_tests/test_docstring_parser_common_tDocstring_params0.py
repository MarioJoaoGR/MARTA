
import pytest
from docstring_parser.common import Docstring

class DocstringParam:
    def __init__(self, name: str, type_: str, description: str):
        self.name = name
        self.type_ = type_
        self.description = description

def test_docstring_initialization():
    doc = Docstring()
    assert doc.short_description is None
    assert doc.long_description is None
    assert not doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert doc.meta == []

def test_docstring_setting_attributes():
    doc = Docstring()
    doc.short_description = "This is a short description."
    doc.long_description = "This provides more detailed information about the function or method."
    doc.blank_after_short_description = True
    doc.blank_after_long_description = True

    assert doc.short_description == "This is a short description."
    assert doc.long_description == "This provides more detailed information about the function or method."
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description

def test_docstring_adding_metadata():
    doc = Docstring()
    param1 = DocstringParam(name="a", type_="int or float", description="First number")
    param2 = DocstringParam(name="b", type_="int or float", description="Second number")

    doc.meta.extend([param1, param2])

    assert len(doc.meta) == 2
    assert isinstance(doc.meta[0], DocstringParam)
    assert isinstance(doc.meta[1], DocstringParam)
    assert doc.meta[0].name == "a"
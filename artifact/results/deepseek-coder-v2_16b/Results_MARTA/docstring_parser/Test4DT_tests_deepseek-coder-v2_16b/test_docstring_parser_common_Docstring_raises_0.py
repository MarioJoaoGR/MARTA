
import pytest
from docstring_parser.common import Docstring, DocstringRaises

def test_docstring_initialization():
    """Test initialization of Docstring class."""
    doc = Docstring()
    assert doc.short_description is None
    assert doc.long_description is None
    assert not doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert len(doc.meta) == 0

def test_add_parameter():
    """Test adding a parameter to the metadata."""
    doc = Docstring()
    class DocstringParam:
        def __init__(self, name, description):
            self.name = name
            self.description = description
    
    param = DocstringParam("parameter_name", "Description of the parameter.")
    doc.meta.append(param)
    
    assert len(doc.meta) == 1
    assert doc.meta[0].name == "parameter_name"
    assert doc.meta[0].description == "Description of the parameter."

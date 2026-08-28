
import pytest
from docstring_parser.numpydoc import NumpydocParser, Section, DEFAULT_SECTIONS, Docstring
import inspect

# Test for parsing a basic numpy-style docstring

# Test for parsing a numpy-style docstring with custom sections

# Test for handling an empty docstring
def test_NumpydocParser_parse_empty():
    parser = NumpydocParser()
    docstring_text = ""
    
    parsed_docstring = parser.parse(docstring_text)
    
    assert isinstance(parsed_docstring, Docstring)
    assert parsed_docstring.short_description is None
    assert len(parsed_docstring.meta) == 0
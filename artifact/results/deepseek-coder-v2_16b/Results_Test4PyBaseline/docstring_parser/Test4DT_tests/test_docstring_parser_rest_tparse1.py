
import pytest
from docstring_parser.rest import parse, Docstring

# Test cases for the `parse` function
def test_empty_docstring():
    text = ""
    parsed_doc = parse(text)
    assert isinstance(parsed_doc, Docstring), "Expected an instance of Docstring"
    assert parsed_doc.short_description is None, "Short description should be None for empty docstring"
    assert parsed_doc.long_description is None, "Long description should be None for empty docstring"
    assert not parsed_doc.meta, "Meta information should be empty for empty docstring"

def test_no_meta():
    text = "This is a short description.\n\nAnd this is a long description with details."
    parsed_doc = parse(text)
    assert isinstance(parsed_doc, Docstring), "Expected an instance of Docstring"
    assert parsed_doc.short_description == 'This is a short description.', "Short description mismatch"
    assert parsed_doc.long_description == 'And this is a long description with details.', "Long description mismatch"

import pytest
from docstring_parser.rest import parse, Docstring, ParseError
import re
import inspect

# Test cases for the `parse` function
def test_parse_empty():
    text = ""
    parsed_doc = parse(text)
    assert isinstance(parsed_doc, Docstring), "Expected an instance of Docstring"
    assert parsed_doc.short_description is None, "Short description should be None for empty string"
    assert parsed_doc.long_description is None, "Long description should be None for empty string"
    assert not parsed_doc.meta, "Meta information should be empty for empty string"

def test_parse_no_meta():
    text = "This is a short description.\n\nAnd this is a long description with details."
    parsed_doc = parse(text)
    assert isinstance(parsed_doc, Docstring), "Expected an instance of Docstring"
    assert parsed_doc.short_description == 'This is a short description.', "Short description mismatch"
    assert parsed_doc.long_description == 'And this is a long description with details.', "Long description mismatch"
    assert not parsed_doc.meta, "Meta information should be empty for docstring without meta"

def test_parse_with_meta():
    text = """This is a short description.
    
    :param param1: Description of param1
    :param param2: Description of param2
    :raises ValueError: If something goes wrong"""
    parsed_doc = parse(text)
    assert isinstance(parsed_doc, Docstring), "Expected an instance of Docstring"
    assert parsed_doc.short_description == 'This is a short description.', "Short description mismatch"
    assert not parsed_doc.long_description, "Long description should be None for docstring with meta but no long description"
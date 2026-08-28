
import pytest
from docstring_parser.rest import parse, Docstring
import re
import inspect

# Test cases for the `parse` function
def test_parse_basic():
    text = "This is a short description.\n\nAnd this is a long description with details."
    parsed_doc = parse(text)
    assert isinstance(parsed_doc, Docstring), "Expected an instance of Docstring"
    assert parsed_doc.short_description == 'This is a short description.', "Short description mismatch"
    assert parsed_doc.long_description == 'And this is a long description with details.', "Long description mismatch"
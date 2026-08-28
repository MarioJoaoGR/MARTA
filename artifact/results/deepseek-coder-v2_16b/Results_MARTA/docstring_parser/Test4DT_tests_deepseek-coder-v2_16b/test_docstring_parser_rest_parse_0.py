
import pytest
from docstring_parser.rest import parse, Docstring, ParseError




def test_no_metadata():
    text = "A brief description\nMore details about the function."
    parsed_doc = parse(text)
    assert parsed_doc.short_description == "A brief description"
    assert parsed_doc.long_description == "More details about the function."
    assert len(parsed_doc.meta) == 0
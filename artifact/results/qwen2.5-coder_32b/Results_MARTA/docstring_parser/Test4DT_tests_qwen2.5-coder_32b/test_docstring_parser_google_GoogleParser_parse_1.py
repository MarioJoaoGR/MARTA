
import pytest
from docstring_parser.google import GoogleParser, ParseError, Section, DocstringMeta, DEFAULT_SECTIONS






def test_parse_empty_docstring():
    parser = GoogleParser()
    docstring_text = ""
    parsed_doc = parser.parse(docstring_text)
    assert parsed_doc.short_description is None
    assert parsed_doc.long_description is None
    assert len(parsed_doc.meta) == 0

def test_parse_only_short_description():
    parser = GoogleParser()
    docstring_text = "Short description."
    parsed_doc = parser.parse(docstring_text)
    assert parsed_doc.short_description == "Short description."
    assert parsed_doc.long_description is None
    assert len(parsed_doc.meta) == 0
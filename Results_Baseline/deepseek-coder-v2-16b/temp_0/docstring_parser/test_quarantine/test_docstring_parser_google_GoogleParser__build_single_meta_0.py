
# Module: docstring_parser.google
# test_googleparser.py
import pytest
from googleparser import GoogleParser, Section
from googleparser import DEFAULT_SECTIONS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, RAISES_KEYWORDS, EXAMPLES_KEYWORDS, PARAM_KEYWORDS
from googleparser import ParseError, DocstringReturns, DocstringRaises, DocstringExample, DocstringMeta

# Test initialization with default sections and title colon enabled
def test_googleparser_default():
    parser = GoogleParser()
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True

# Test initialization with custom sections and title colon disabled
def test_googleparser_custom():
    sec1 = Section("Parameters", "These are the parameters.")
    sec2 = Section("Returns", "This is the return section.")
    parser = GoogleParser([sec1, sec2], title_colon=False)
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is False

# Test initialization with custom sections and title colon enabled
def test_googleparser_custom_with_colon():
    sec1 = Section("Parameters", "These are the parameters.")
    sec2 = Section("Returns", "This is the return section.")
    parser = GoogleParser([sec1, sec2], title_colon=True)
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True

# Test initialization with no sections provided (should default to DEFAULT_SECTIONS)
def test_googleparser_no_sections():
    parser = GoogleParser(sections=None, title_colon=True)
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
    assert parser.title_colon is True

# Test initialization with invalid section type raises TypeError
def test_googleparser_invalid_section_type():
    sec1 = "InvalidSection"
    with pytest.raises(TypeError):
        GoogleParser([sec1], title_colon=True)

# Test _build_single_meta method for Returns keyword
def test_build_single_meta_returns():
    section = Section("Returns", "This is the return value.")
    meta = GoogleParser._build_single_meta(section, "This is the description.")
    assert isinstance(meta, DocstringReturns)
    assert meta.args == ["Returns"]
    assert meta.description == "This is the description."

# Test _build_single_meta method for Raises keyword
def test_build_single_meta_raises():
    section = Section("Raises", "This is a raised exception.")
    meta = GoogleParser._build_single_meta(section, "This is the description.")
    assert isinstance(meta, DocstringRaises)
    assert meta.args == ["Raises"]
    assert meta.description == "This is the description."

# Test _build_single_meta method for Examples keyword
def test_build_single_meta_examples():
    section = Section("Examples", "These are examples.")
    meta = GoogleParser._build_single_meta(section, "This is the example description.")
    assert isinstance(meta, DocstringExample)
    assert meta.args == ["Examples"]
    assert meta.description == "This is the example description."

# Test _build_single_meta method for Parameters keyword raises ParseError
def test_build_single_meta_parameters():
    section = Section("Parameters", "These are parameters.")
    with pytest.raises(ParseError):
        GoogleParser._build_single_meta(section, "This is the parameter description.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_GoogleParser__build_single_meta_0
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_0.py:5:0: E0401: Unable to import 'googleparser' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_0.py:6:0: E0401: Unable to import 'googleparser' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_0.py:7:0: E0401: Unable to import 'googleparser' (import-error)

"""
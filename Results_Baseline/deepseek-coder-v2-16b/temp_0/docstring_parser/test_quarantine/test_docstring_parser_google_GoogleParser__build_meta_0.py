
# Module: docstring_parser.google
# test_googleparser.py
import pytest
from googleparser import GoogleParser, Section, DEFAULT_SECTIONS
try:
    from googleparser import ParseError
except ImportError:
    class ParseError(Exception): pass

def test_default_sections():
    parser = GoogleParser()
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
    for section in DEFAULT_SECTIONS:
        assert section.title in parser.sections

@pytest.mark.parametrize("custom_sections, expected", [
    ([Section('Summary', 'summary')], 1),
    ([Section('Arguments', 'arguments'), Section('Returns', 'returns')], 2)
])
def test_custom_sections(custom_sections, expected):
    parser = GoogleParser(sections=custom_sections)
    assert len(parser.sections) == expected
    for section in custom_sections:
        assert section.title in parser.sections

@pytest.mark.parametrize("title_colon", [True, False])
def test_title_colon(title_colon):
    sections = [Section('Parameters', 'parameters')]
    parser = GoogleParser(sections=sections, title_colon=title_colon)
    assert parser.title_colon == title_colon

@pytest.mark.parametrize("sections, title_colon", [
    ([], True),
    ([Section('Parameters', 'parameters')], False)
])
def test_setup(sections, title_colon):
    parser = GoogleParser(sections=sections, title_colon=title_colon)
    assert parser.title_colon == title_colon
    if sections:
        for section in sections:
            assert section.title in parser.sections

def test_parse_error():
    with pytest.raises(ParseError):
        GoogleParser()._build_meta("No colon here", "Parameters")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_GoogleParser__build_meta_0
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_meta_0.py:5:0: E0401: Unable to import 'googleparser' (import-error)

"""
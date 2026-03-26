
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS, ParseError, SectionType

@pytest.fixture
def parser():
    return GoogleParser()

def test_valid_input(parser):
    sec1 = Section("Summary", "This is the summary.")
    assert sec1.title == "Summary"
    assert sec1.content == "This is the summary."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_GoogleParser__build_meta_1_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_meta_1_test_valid_input.py:12:11: E1101: Instance of 'Section' has no 'content' member (no-member)


"""
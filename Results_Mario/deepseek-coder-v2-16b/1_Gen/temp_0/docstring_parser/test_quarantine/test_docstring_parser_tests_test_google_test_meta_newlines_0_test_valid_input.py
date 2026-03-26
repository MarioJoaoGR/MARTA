
import pytest
from docstring_parser.tests.test_google import parse, SectionType

def test_meta_newlines(
    source: str,
    expected_short_desc: T.Optional[str],
    expected_long_desc: T.Optional[str],
    expected_blank_short_desc: bool,
    expected_blank_long_desc: bool,
) -> None:
    """Test parsing newlines around description sections."""
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc
    assert len(docstring.meta) == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_meta_newlines_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_valid_input.py:7:25: E0602: Undefined variable 'T' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_valid_input.py:8:24: E0602: Undefined variable 'T' (undefined-variable)

"""
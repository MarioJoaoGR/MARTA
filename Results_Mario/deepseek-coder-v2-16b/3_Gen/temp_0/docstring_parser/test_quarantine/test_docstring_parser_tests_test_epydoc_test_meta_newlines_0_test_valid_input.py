
import pytest
from docstring_parser import parse

def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc):
    """Test parsing newlines around description sections."""
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_meta_newlines_0_test_valid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
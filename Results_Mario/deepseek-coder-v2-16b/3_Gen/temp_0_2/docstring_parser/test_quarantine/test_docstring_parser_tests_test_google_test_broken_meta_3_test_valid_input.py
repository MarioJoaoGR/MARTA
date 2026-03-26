
import pytest
from docstring_parser import parse, ParseError

def test_valid_input():
    """Test parsing broken meta."""
    with pytest.raises(ParseError):
        parse("Args:")

    with pytest.raises(ParseError):
        parse("Args:\n    herp derp")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_broken_meta_3_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_broken_meta_3_test_valid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_broken_meta_3_test_valid_input.py:3:0: E0611: No name 'ParseError' in module 'docstring_parser' (no-name-in-module)


"""
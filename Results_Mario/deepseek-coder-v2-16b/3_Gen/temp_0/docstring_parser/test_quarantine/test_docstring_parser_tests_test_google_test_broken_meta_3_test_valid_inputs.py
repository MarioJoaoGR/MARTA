
import pytest
from docstring_parser.tests.test_google import parse
from docstring_parser.exceptions import ParseError

def test_broken_meta() -> None:
    """Test parsing broken meta."""
    with pytest.raises(ParseError):
        parse("Args:")

    with pytest.raises(ParseError):
        parse("Args:\n    herp derp")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_broken_meta_3_test_valid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_broken_meta_3_test_valid_inputs.py:4:0: E0401: Unable to import 'docstring_parser.exceptions' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_broken_meta_3_test_valid_inputs.py:4:0: E0611: No name 'exceptions' in module 'docstring_parser' (no-name-in-module)


"""
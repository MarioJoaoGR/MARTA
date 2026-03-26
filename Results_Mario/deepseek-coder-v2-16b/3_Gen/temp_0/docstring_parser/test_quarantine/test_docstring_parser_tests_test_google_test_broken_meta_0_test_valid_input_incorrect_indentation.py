
import pytest
from googleparser import parse

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
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_broken_meta_0_test_valid_input_incorrect_indentation
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_broken_meta_0_test_valid_input_incorrect_indentation.py:3:0: E0401: Unable to import 'googleparser' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_broken_meta_0_test_valid_input_incorrect_indentation.py:7:23: E0602: Undefined variable 'ParseError' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_broken_meta_0_test_valid_input_incorrect_indentation.py:10:23: E0602: Undefined variable 'ParseError' (undefined-variable)


"""
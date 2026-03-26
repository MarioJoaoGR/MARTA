
import pytest
from docstring_parser.tests.test_epydoc import parse
from docstring_parser.exceptions import ParseError

def test_broken_meta() -> None:
    """Test parsing broken meta."""
    with pytest.raises(ParseError):
        parse("@")

    with pytest.raises(ParseError):
        parse("@param herp derp")

    with pytest.raises(ParseError):
        parse("@param: invalid")

    with pytest.raises(ParseError):
        parse("@param with too many args: desc")

    # these should not raise any errors
    parse("@sthstrange: desc")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_broken_meta_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_broken_meta_0_test_valid_input.py:4:0: E0401: Unable to import 'docstring_parser.exceptions' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_broken_meta_0_test_valid_input.py:4:0: E0611: No name 'exceptions' in module 'docstring_parser' (no-name-in-module)


"""
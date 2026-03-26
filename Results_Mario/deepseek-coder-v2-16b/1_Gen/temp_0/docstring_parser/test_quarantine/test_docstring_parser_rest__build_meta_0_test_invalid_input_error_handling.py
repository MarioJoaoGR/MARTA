
import pytest
from docstring_parser.rest import DocstringMeta, ParseError

def test_invalid_input_error_handling():
    with pytest.raises(ParseError):
        _build_meta(["param1", "int", "example_arg"], "This parameter is used to set up the example.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_invalid_input_error_handling
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_invalid_input_error_handling.py:7:8: E0602: Undefined variable '_build_meta' (undefined-variable)

"""
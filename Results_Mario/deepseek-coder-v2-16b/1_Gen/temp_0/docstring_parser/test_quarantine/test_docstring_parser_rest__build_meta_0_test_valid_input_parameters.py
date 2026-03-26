
import pytest
from docstring_parser.rest import DocstringMeta, ParseError, PARAM_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, DEPRECATION_KEYWORDS, RAISES_KEYWORDS

def test_valid_input_parameters():
    # Test with parameter meta information
    meta = _build_meta(args=["param1", "int", "example_arg"], desc="This parameter is used to set up the example.")
    
    assert meta.args == ["param1", "int", "example_arg"]
    assert meta.description == "This parameter is used to set up the example."
    assert meta.arg_name == "example_arg"
    assert meta.type_name == "int"
    assert meta.is_optional == False
    assert meta.default is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_valid_input_parameters
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_input_parameters.py:7:11: E0602: Undefined variable '_build_meta' (undefined-variable)

"""
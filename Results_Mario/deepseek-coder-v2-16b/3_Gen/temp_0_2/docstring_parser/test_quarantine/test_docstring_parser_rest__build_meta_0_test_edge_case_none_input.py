
import pytest
from docstring_parser.rest import DocstringMeta, ParseError

# Assuming these constants and keywords are defined in your module or context
PARAM_KEYWORDS = ["param1", "param2"]
RETURNS_KEYWORDS = ["return"]
YIELDS_KEYWORDS = ["yield"]
DEPRECATION_KEYWORDS = ["deprecated"]
RAISES_KEYWORDS = ["raises"]

def test_edge_case_none_input():
    # Test when args is None and desc is an empty string
    with pytest.raises(ParseError):
        _build_meta(args=None, desc="")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_edge_case_none_input
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:15:8: E0602: Undefined variable '_build_meta' (undefined-variable)


"""
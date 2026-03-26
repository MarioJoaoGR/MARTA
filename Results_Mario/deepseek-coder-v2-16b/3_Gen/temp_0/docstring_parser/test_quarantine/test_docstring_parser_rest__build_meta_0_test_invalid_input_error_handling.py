
import pytest
from docstring_parser.rest import DocstringMeta, ParseError
import typing as T

# Assuming these are defined in the module you're testing
PARAM_KEYWORDS = []  # Define this appropriately
RETURNS_KEYWORDS = []  # Define this appropriately
YIELDS_KEYWORDS = []  # Define this appropriately
DEPRECATION_KEYWORDS = []  # Define this appropriately
RAISES_KEYWORDS = []  # Define this appropriately

def test_invalid_input_error_handling():
    with pytest.raises(ParseError) as excinfo:
        _build_meta(args=["param1"], desc="This parameter is used to set up the example.")
    assert str(excinfo.value) == "Expected one or two arguments for a param1 keyword."

    with pytest.raises(ParseError) as excinfo:
        _build_meta(args=["param1", "int", "example_arg"], desc="This parameter is used to set up the example.")
    assert str(excinfo.value) == "Expected one or two arguments for a param1 keyword."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_invalid_input_error_handling
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_invalid_input_error_handling.py:15:8: E0602: Undefined variable '_build_meta' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_invalid_input_error_handling.py:19:8: E0602: Undefined variable '_build_meta' (undefined-variable)


"""
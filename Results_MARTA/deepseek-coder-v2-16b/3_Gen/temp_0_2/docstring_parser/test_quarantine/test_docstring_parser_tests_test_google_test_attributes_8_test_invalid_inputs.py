
import pytest
from docstring_parser.tests.test_google import parse

def test_invalid_inputs() -> None:
    """Test invalid inputs to check error handling."""
    with pytest.raises(ValueError):
        parse("Short description", strict=True)

    with pytest.raises(ValueError):
        parse("Short description\n\nAttributes:\n    name: description 1")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_attributes_8_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_attributes_8_test_invalid_inputs.py:8:8: E1123: Unexpected keyword argument 'strict' in function call (unexpected-keyword-arg)


"""
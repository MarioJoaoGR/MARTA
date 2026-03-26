
import pytest
from docstring_parser import parse

def test_invalid_input() -> None:
    """Test handling invalid input gracefully."""
    with pytest.raises(ValueError):
        parse(":deprecation: this function will be removed")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_deprecation_5_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_deprecation_5_test_invalid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
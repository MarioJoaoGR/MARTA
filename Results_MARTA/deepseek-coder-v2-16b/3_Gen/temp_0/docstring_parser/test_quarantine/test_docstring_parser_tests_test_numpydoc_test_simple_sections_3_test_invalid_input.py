
import pytest
from docstring_parser import parse

def test_invalid_input():
    with pytest.raises(ValueError):
        parse("Short description")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_simple_sections_3_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_simple_sections_3_test_invalid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""
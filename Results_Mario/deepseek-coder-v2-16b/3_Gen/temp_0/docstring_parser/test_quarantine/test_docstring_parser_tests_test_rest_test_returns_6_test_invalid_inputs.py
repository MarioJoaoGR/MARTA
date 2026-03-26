
import pytest
from docstring_parser import parse

def test_invalid_inputs():
    with pytest.raises(Exception):
        docstring = parse("Invalid Docstring")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_returns_6_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_returns_6_test_invalid_inputs.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)


"""

import pytest
from your_module import parse, compose

def test_short_rtype() -> None:
    """Test abbreviated docstring with only return type information."""
    string = "Short description.\n\n@rtype: float"
    docstring = parse(string)
    assert compose(docstring) == string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_epydoc_test_short_rtype_2_test_empty_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_rtype_2_test_empty_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""
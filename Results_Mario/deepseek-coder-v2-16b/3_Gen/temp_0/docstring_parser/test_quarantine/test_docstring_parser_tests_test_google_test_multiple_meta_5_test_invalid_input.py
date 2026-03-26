
import pytest
from googleparser import parse

def test_multiple_meta():
    with pytest.raises(ValueError):
        docstring = parse("Invalid docstring content\n\nArgs:\n    spam: asd\n        1\n            2\n        3\n\nRaises:\n    bla: herp\n    yay: derp\n")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_multiple_meta_5_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_multiple_meta_5_test_invalid_input.py:3:0: E0401: Unable to import 'googleparser' (import-error)


"""
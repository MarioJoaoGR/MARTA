
# Module: docstring_parser.tests.test_google
import pytest
from docstring_parser.tests import test_multiple_meta as tmm

def test_multiple_meta():
    """Test parsing multiple meta."""
    # Call the function to be tested
    tmm.test_multiple_meta()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_multiple_meta_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_multiple_meta_0.py:4:0: E0611: No name 'test_multiple_meta' in module 'docstring_parser.tests' (no-name-in-module)

"""

import pytest
from docstring_parser.rest import process_desc, RenderingStyle

def test_invalid_style():
    # Test when rendering style is not recognized
    assert process_desc("Test description", "INVALID") == " Test description"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest_process_desc_0_test_invalid_style
docstring_parser/Test4DT_tests/test_docstring_parser_rest_process_desc_0_test_invalid_style.py:3:0: E0611: No name 'process_desc' in module 'docstring_parser.rest' (no-name-in-module)


"""
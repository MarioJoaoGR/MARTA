
import pytest
from docstring_parser.google import process_one
from docstring_parser.structures import DocstringParam, RenderingStyle

def test_process_one():
    # Create a mock DocstringParam object for testing
    doc_obj = DocstringParam(arg_name="example_param", type_name="int", description="This is an example parameter.", is_optional=False)
    
    # Call the process_one function with the mock object
    parts = []  # Initialize an empty list to hold the parts of the docstring
    process_one(doc_obj, parts=parts)
    
    # Check that the output matches the expected result
    assert len(parts) == 1
    assert parts[0] == "example_param (int):"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_process_one_0_test_valid_input_param
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_param.py:3:0: E0611: No name 'process_one' in module 'docstring_parser.google' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_param.py:4:0: E0401: Unable to import 'docstring_parser.structures' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_param.py:4:0: E0611: No name 'structures' in module 'docstring_parser' (no-name-in-module)

"""
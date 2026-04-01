
import pytest
from docstring_parser.google import process_one, DocstringParam, RenderingStyle

def test_valid_input_param():
    # Create a mock DocstringParam object
    doc_obj = DocstringParam(arg_name="example_param", type_name="int", description="This is an example parameter.", is_optional=False)
    
    # Initialize the parts list (this should be mocked or initialized properly in the function)
    parts = []
    
    # Call the process_one function with the mock object
    process_one(doc_obj, parts=parts)
    
    # Check that the parts list has been updated correctly
    assert len(parts) == 1
    assert parts[0] == "example_param (int):" if RenderingStyle.COMPACT else "example_param (int), optional:"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_process_one_0_test_valid_input_param
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_param.py:3:0: E0611: No name 'process_one' in module 'docstring_parser.google' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_param.py:7:14: E1120: No value for argument 'args' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_google_process_one_0_test_valid_input_param.py:7:14: E1120: No value for argument 'default' in constructor call (no-value-for-parameter)


"""
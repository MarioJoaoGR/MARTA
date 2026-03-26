
# Module: docstring_parser.util
import pytest
from docstring_parser.util import wrapper  # Corrected import statement

# Define example functions with their respective docstrings
def test_function():
    '''This is a test function'''
    pass

def another_test_function():
    '''This is another test function'''
    pass

# Test cases for the wrapper function
def test_wrapper_single_function():
    combined_doc = wrapper(test_function)
    assert combined_doc.__doc__ == 'This is a test function'

def test_wrapper_chaining_functions():
    combined_doc = wrapper(test_function)
    combined_doc = wrapper(combined_doc, another_test_function)
    assert combined_doc.__doc__ == ('This is a test function\n\n'
                                    'This is another test function')

def test_wrapper_no_additional_functions():
    combined_doc = wrapper(test_function)
    assert combined_doc.__doc__ == 'This is a test function'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_util_wrapper_0
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0.py:4:0: E0611: No name 'wrapper' in module 'docstring_parser.util' (no-name-in-module)

"""
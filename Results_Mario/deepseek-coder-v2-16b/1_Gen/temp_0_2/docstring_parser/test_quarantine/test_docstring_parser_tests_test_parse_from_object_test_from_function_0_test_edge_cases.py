
import pytest
from docstring_parser import parse_from_object

def a_function(param1: str, param2: int = 2):
    """Short description
    Args:
        param1: Description for param1
        param2: Description for param2
    """
    return f"{param1} {param2}"

def test_from_function():
    docstring = parse_from_object(a_function)
    
    assert docstring.short_description == "Short description"
    assert docstring.description == "Short description"
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "param1"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "Description for param1"
    assert docstring.params[1].arg_name == "param2"
    assert docstring.params[1].type_name is None
    assert docstring.params[1].description == "Description for param2"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_test_from_function_0_test_edge_cases
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_test_from_function_0_test_edge_cases.py:3:0: E0611: No name 'parse_from_object' in module 'docstring_parser' (no-name-in-module)


"""
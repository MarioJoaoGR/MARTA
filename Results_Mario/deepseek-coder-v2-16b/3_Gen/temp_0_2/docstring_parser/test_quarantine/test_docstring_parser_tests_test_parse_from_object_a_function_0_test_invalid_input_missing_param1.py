
import pytest
from docstring_parser import parse

def a_function(param1: str, param2: int = 2):
    """Short description
    Args:
        param1 (str): Description for param1
        param2 (int, optional): Description for param2
    Returns:
        str: A string that concatenates the values of `param1` and `param2`.
    """
    return f"{param1} {param2}"

def test_invalid_input_missing_param1():
    with pytest.raises(TypeError):
        a_function()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_a_function_0_test_invalid_input_missing_param1
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_a_function_0_test_invalid_input_missing_param1.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_a_function_0_test_invalid_input_missing_param1.py:17:8: E1120: No value for argument 'param1' in function call (no-value-for-parameter)


"""
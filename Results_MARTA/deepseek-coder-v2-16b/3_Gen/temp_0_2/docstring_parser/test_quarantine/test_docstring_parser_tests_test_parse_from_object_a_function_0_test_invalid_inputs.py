
import pytest
from docstring_parser import parse

def a_function(param1: str, param2: int = 2):
    """Short description
    Args:
        param1: Description for param1
        param2: Description for param2
    """
    return f"{param1} {param2}"

# Test case to check invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        a_function()  # Calling without arguments should raise TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_a_function_0_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_a_function_0_test_invalid_inputs.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_a_function_0_test_invalid_inputs.py:16:8: E1120: No value for argument 'param1' in function call (no-value-for-parameter)


"""

import pytest
from docstring_parser.tests.test_parse_from_object import parse

def a_function(param1: str, param2: int = 2) -> str:
    """
    A function that takes two parameters and returns their combination as a string. The function can be called with either positional arguments or keyword arguments. If `param2` is not provided, it defaults to 2.
    
    Args:
        param1 (str): The first parameter, which is expected to be a string. This parameter is required.
        param2 (int, optional): The second parameter, which defaults to 2 if not provided. It is an integer.
        
    Returns:
        str: A string that concatenates the values of `param1` and `param2`.
    
    Examples:
        >>> a_function("Hello")
        'Hello 2'
        >>> a_function("Hello", 3)
        'Hello 3'
        >>> a_function(param2=5, param1="Hi")
        'Hi 5'
    
    Notes:
        - The function can be called with either positional arguments or keyword arguments.
        - If `param2` is not provided, it defaults to 2.
        - The return value is a string that combines the values of `param1` and `param2`.
    """

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_a_function_0_test_edge_cases
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_a_function_0_test_edge_cases.py:3:0: E0611: No name 'parse' in module 'docstring_parser.tests.test_parse_from_object' (no-name-in-module)


"""
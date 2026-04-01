
from docstring_parser import parse
from docstring_parser.util import DocstringParam, chain, compose
import pytest

def test_valid_inputs():
    def func1():
        '''Function 1 description'''
        pass
    
    def func2():
        '''Function 2 description'''
        pass
    
    combined_func = wrapper(func1)
    assert combined_func.__doc__ == func1.__doc__
    
    combined_func = wrapper(func2)
    assert combined_func.__doc__ == func2.__doc__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_util_wrapper_0_test_valid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:15:20: E0602: Undefined variable 'wrapper' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:18:20: E0602: Undefined variable 'wrapper' (undefined-variable)


"""
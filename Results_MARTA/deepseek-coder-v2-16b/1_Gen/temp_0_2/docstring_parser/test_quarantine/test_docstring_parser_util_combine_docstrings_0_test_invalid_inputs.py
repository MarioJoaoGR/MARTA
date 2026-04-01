
from docstring_parser import parse, DocstringStyle, RenderingStyle
from docstring_parser.util import _DocstringMeta, combine_docstrings
import typing as T
from inspect import Signature
from collections import ChainMap
from itertools import chain

def test_invalid_inputs():
    def fun1(a, b, c, d):
        '''short_description: fun1
        
        :param a: fun1
        :param b: fun1
        :return: fun1
        '''
    
    def fun2(b, c, d, e):
        '''short_description: fun2
        
        long_description: fun2
        
        :param b: fun2
        :param c: fun2
        :param e: fun2
        '''
    
    @combine_docstrings(fun1, fun2)
    def decorated(a, b, c, d, e, f):
        '''
        :param e: decorated
        :param f: decorated
        '''
    
    assert decorated.__doc__ == """
short_description: fun2
<BLANKLINE>
long_description: fun2
<BLANKLINE>
:param a: fun1
:param b: fun1
:param c: fun2
:param e: fun2
:param f: decorated
:returns: fun1"""
    
    @combine_docstrings(fun1, fun2, exclude=[DocstringReturns])
    def decorated(a, b, c, d, e, f): pass
    
    assert decorated.__doc__ == """
short_description: fun2
<BLANKLINE>
long_description: fun2
<BLANKLINE>
:param a: fun1
:param b: fun1
:param c: fun2
:param e: fun2"""

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_util_combine_docstrings_0_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_invalid_inputs.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_invalid_inputs.py:2:0: E0611: No name 'DocstringStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_invalid_inputs.py:2:0: E0611: No name 'RenderingStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_invalid_inputs.py:3:0: E0611: No name '_DocstringMeta' in module 'docstring_parser.util' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_invalid_inputs.py:48:4: E0102: function already defined line 29 (function-redefined)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_invalid_inputs.py:47:45: E0602: Undefined variable 'DocstringReturns' (undefined-variable)


"""
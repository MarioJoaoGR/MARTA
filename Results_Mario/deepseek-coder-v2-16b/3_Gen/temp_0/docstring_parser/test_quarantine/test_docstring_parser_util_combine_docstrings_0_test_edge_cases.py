
import pytest
from docstring_parser.util import combine_docstrings, DocstringStyle, RenderingStyle
from typing import Callable as _Func, Iterable as T

# Assuming these are defined somewhere in your module or standard library
class DocstringMeta: pass
class DocstringParam(DocstringMeta): pass
class DocstringReturns(DocstringMeta): pass

def test_combine_docstrings():
    def fun1(a, b, c, d):
        '''short_description: fun1

        :param a: fun1
        :param b: fun1
        :return: fun1
        '''
        pass

    def fun2(b, c, d, e):
        '''short_description: fun2

        long_description: fun2

        :param b: fun2
        :param c: fun2
        :param e: fun2
        '''
        pass

    @combine_docstrings(fun1, fun2)
    def decorated(a, b, c, d, e, f):
        '''
        :param e: decorated
        :param f: decorated
        '''
        pass

    assert decorated.__doc__ == """
short_description: fun2
<BLANKLINE>
long_description: fun2
<BLANKLINE>
:param a: fun1
:param b: fun1
:param c: fun2
:param e: fun2
:param f: decorated"""

    @combine_docstrings(fun1, fun2, exclude=[DocstringReturns])
    def decorated_exclude(a, b, c, d, e, f):
        pass

    assert decorated_exclude.__doc__ == """
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
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________ test_combine_docstrings ____________________________

    def test_combine_docstrings():
        def fun1(a, b, c, d):
            '''short_description: fun1
    
            :param a: fun1
            :param b: fun1
            :return: fun1
            '''
            pass
    
        def fun2(b, c, d, e):
            '''short_description: fun2
    
            long_description: fun2
    
            :param b: fun2
            :param c: fun2
            :param e: fun2
            '''
            pass
    
        @combine_docstrings(fun1, fun2)
        def decorated(a, b, c, d, e, f):
            '''
            :param e: decorated
            :param f: decorated
            '''
            pass
    
>       assert decorated.__doc__ == """
    short_description: fun2
    <BLANKLINE>
    long_description: fun2
    <BLANKLINE>
    :param a: fun1
    :param b: fun1
    :param c: fun2
    :param e: fun2
    :param f: decorated"""
E       AssertionError: assert 'short_descri...returns: fun1' == '\nshort_desc... f: decorated'
E         
E         + short_description: fun2
E           
E         - short_description: fun2
E         - <BLANKLINE>
E           long_description: fun2
E         - <BLANKLINE>...
E         
E         ...Full output truncated (9 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_edge_cases.py:40: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_edge_cases.py::test_combine_docstrings
============================== 1 failed in 0.08s ===============================
"""

import pytest
from docstring_parser.util import combine_docstrings, DocstringStyle, RenderingStyle

def fun1(a, b, c, d):
    """short_description: fun1

    :param a: fun1
    :param b: fun1
    :return: fun1
    """
    pass

def fun2(b, c, d, e):
    """short_description: fun2

    long_description: fun2

    :param b: fun2
    :param c: fun2
    :param e: fun2
    """
    pass

@combine_docstrings(fun1, fun2)
def decorated(a, b, c, d, e, f):
    """
    :param e: decorated
    :param f: decorated
    """
    pass

def test_combine_docstrings():
    assert decorated.__doc__ == (
        "short_description: fun2\n"
        "\n"
        "long_description: fun2\n"
        "\n"
        ":param a: fun1\n"
        ":param b: fun1\n"
        ":param c: fun2\n"
        ":param e: fun2\n"
    )

@combine_docstrings(fun1, fun2, exclude=[DocstringReturns])
def decorated_excluded(a, b, c, d, e, f):
    """
    :param e: decorated
    :param f: decorated
    """
    pass

def test_combine_docstrings_exclude():
    assert decorated_excluded.__doc__ == (
        "short_description: fun2\n"
        "\n"
        "long_description: fun2\n"
        "\n"
        ":param a: fun1\n"
        ":param b: fun1\n"
        ":param c: fun2\n"
        ":param e: fun2\n"
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_util_combine_docstrings_0_test_edge_cases
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_edge_cases.py:45:41: E0602: Undefined variable 'DocstringReturns' (undefined-variable)

"""
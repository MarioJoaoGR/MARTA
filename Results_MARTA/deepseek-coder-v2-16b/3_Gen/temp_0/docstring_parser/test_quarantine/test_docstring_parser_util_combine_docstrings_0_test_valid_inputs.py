
import pytest
from docstring_parser.util import combine_docstrings, DocstringParam, DocstringReturns, DocstringStyle, RenderingStyle

@pytest.fixture
def fun1():
    def func(a, b, c, d):
        """short_description: fun1

        :param a: fun1
        :param b: fun1
        :return: fun1
        """
        pass
    return func

@pytest.fixture
def fun2():
    def func(b, c, d, e):
        """short_description: fun2

        long_description: fun2

        :param b: fun2
        :param c: fun2
        :param e: fun2
        """
        pass
    return func

def test_combine_docstrings(fun1, fun2):
    @combine_docstrings(fun1, fun2)
    def decorated(a, b, c, d, e, f):
        """
        :param e: decorated
        :param f: decorated
        """
        pass

    assert decorated.__doc__ == (
        "short_description: fun2\n"
        "\n"
        "long_description: fun2\n"
        "\n"
        ":param a: fun1\n"
        ":param b: fun1\n"
        ":param c: fun2\n"
        ":param e: fun2\n"
        ":param f: decorated\n"
        ":returns: fun1"
    )

def test_combine_docstrings_exclude(fun1, fun2):
    @combine_docstrings(fun1, fun2, exclude=[DocstringReturns])
    def decorated(a, b, c, d, e, f):
        pass

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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_combine_docstrings_exclude ________________________

fun1 = <function fun1.<locals>.func at 0x1020f4700>
fun2 = <function fun2.<locals>.func at 0x1020f4b80>

    def test_combine_docstrings_exclude(fun1, fun2):
        @combine_docstrings(fun1, fun2, exclude=[DocstringReturns])
        def decorated(a, b, c, d, e, f):
            pass
    
>       assert decorated.__doc__ == (
            "short_description: fun2\n"
            "\n"
            "long_description: fun2\n"
            "\n"
            ":param a: fun1\n"
            ":param b: fun1\n"
            ":param c: fun2\n"
            ":param e: fun2\n"
        )
E       AssertionError: assert 'short_descri...param e: fun2' == 'short_descri...ram e: fun2\n'
E         
E         Skipping 97 identical leading characters in diff, use -v to show
E         - ram e: fun2
E         ?            -
E         + ram e: fun2

docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py:58: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py::test_combine_docstrings_exclude
========================= 1 failed, 1 passed in 0.08s ==========================
"""
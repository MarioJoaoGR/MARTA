
import pytest
from docstring_parser.tests.test_util import combine_docstrings, DocstringParam, DocstringReturns

def test_combine_docstrings() -> None:
    """Test combine_docstrings wrapper."""

    def fun1(arg_a, arg_b, arg_c, arg_d):
        """short_description: fun1

        :param arg_a: fun1
        :param arg_b: fun1
        :return: fun1
        """
        assert arg_a and arg_b and arg_c and arg_d

    def fun2(arg_b, arg_c, arg_d, arg_e):
        """short_description: fun2

        long_description: fun2

        :param arg_b: fun2
        :param arg_c: fun2
        :param arg_e: fun2
        """
        assert arg_b and arg_c and arg_d and arg_e

    @combine_docstrings(fun1, fun2)
    def decorated1(arg_a, arg_b, arg_c, arg_d, arg_e, arg_f):
        """
        :param arg_e: decorated
        :param arg_f: decorated
        """
        assert arg_a and arg_b and arg_c and arg_d and arg_e and arg_f

    assert decorated1.__doc__ == (
        "short_description: fun2\n"
        "\n"
        "long_description: fun2\n"
        "\n"
        ":param arg_a: fun1\n"
        ":param arg_b: fun1\n"
        ":param arg_c: fun2\n"
        ":param arg_e: fun2\n"
        ":param arg_f: decorated\n"
        ":returns: fun1"
    )

    @combine_docstrings(fun1, fun2, exclude=[DocstringReturns])
    def decorated2(arg_a, arg_b, arg_c, arg_d, arg_e, arg_f):
        assert arg_a and arg_b and arg_c and arg_d and arg_e and arg_f

    assert decorated2.__doc__ == (
        "short_description: fun2\n"
        "\n"
        "long_description: fun2\n"
        "\n"
        ":param arg_a: fun1\n"
        ":param arg_b: fun1\n"
        ":param arg_c: fun2\n"
        ":param arg_e: fun2\n"
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_util_test_combine_docstrings_0_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_util_test_combine_docstrings_0_test_invalid_inputs.py:3:0: E0611: No name 'DocstringParam' in module 'docstring_parser.tests.test_util' (no-name-in-module)


"""
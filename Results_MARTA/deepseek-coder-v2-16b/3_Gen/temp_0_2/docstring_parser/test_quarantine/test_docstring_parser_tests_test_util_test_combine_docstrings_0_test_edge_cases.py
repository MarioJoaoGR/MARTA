
from docstring_parser.tests.test_util import combine_docstrings, DocstringReturns

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
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_util_test_combine_docstrings_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________ test_combine_docstrings ____________________________

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
    
>       assert decorated2.__doc__ == (
            "short_description: fun2\n"
            "\n"
            "long_description: fun2\n"
            "\n"
            ":param arg_a: fun1\n"
            ":param arg_b: fun1\n"
            ":param arg_c: fun2\n"
            ":param arg_e: fun2\n"
        )
E       AssertionError: assert 'short_descri...m arg_e: fun2' == 'short_descri...arg_e: fun2\n'
E         
E         Skipping 113 identical leading characters in diff, use -v to show
E         - arg_e: fun2
E         ?            -
E         + arg_e: fun2

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_util_test_combine_docstrings_0_test_edge_cases.py:52: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_util_test_combine_docstrings_0_test_edge_cases.py::test_combine_docstrings
============================== 1 failed in 0.05s ===============================
"""

import pytest
from docstring_parser.tests.test_epydoc import parse, compose, RenderingStyle

@pytest.mark.parametrize("source, expected", [
    (
        "Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n",
        "A formatted string with detailed information including parameter descriptions and return types."
    )
])
def test_compose_expanded(source, expected):
    """Test compose in expanded mode."""
    assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_expanded_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_ test_compose_expanded[Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n-A formatted string with detailed information including parameter descriptions and return types.] _

source = 'Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n'
expected = 'A formatted string with detailed information including parameter descriptions and return types.'

    @pytest.mark.parametrize("source, expected", [
        (
            "Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n",
            "A formatted string with detailed information including parameter descriptions and return types."
        )
    ])
    def test_compose_expanded(source, expected):
        """Test compose in expanded mode."""
>       assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected
E       AssertionError: assert 'Example func...the operation' == 'A formatted ...return types.'
E         
E         - A formatted string with detailed information including parameter descriptions and return types.
E         + Example function to demonstrate parsing.
E         + @param arg1:
E         +     The first argument
E         + @return:
E         +     The result of the operation

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_expanded_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_expanded_0_test_valid_input.py::test_compose_expanded[Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n-A formatted string with detailed information including parameter descriptions and return types.]
============================== 1 failed in 0.03s ===============================

"""

import pytest
from docstring_parser.tests.test_epydoc import compose, parse

@pytest.mark.parametrize("source, expected", [
    ("Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n", "Example function to demonstrate parsing.\nThe first argument\nThe result of the operation"),
])
def test_invalid_input(source, expected):
    assert compose(parse(source)) == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_ test_invalid_input[Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n-Example function to demonstrate parsing.\nThe first argument\nThe result of the operation] _

source = 'Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n'
expected = 'Example function to demonstrate parsing.\nThe first argument\nThe result of the operation'

    @pytest.mark.parametrize("source, expected", [
        ("Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n", "Example function to demonstrate parsing.\nThe first argument\nThe result of the operation"),
    ])
    def test_invalid_input(source, expected):
>       assert compose(parse(source)) == expected
E       AssertionError: assert 'Example func...the operation' == 'Example func...the operation'
E         
E           Example function to demonstrate parsing.
E         - The first argument
E         + @param arg1: The first argument
E         - The result of the operation
E         + @return: The result of the operation
E         ? +++++++++

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_invalid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_invalid_input.py::test_invalid_input[Example function to demonstrate parsing.\n@param arg1: The first argument\n@return: The result of the operation\n-Example function to demonstrate parsing.\nThe first argument\nThe result of the operation]
============================== 1 failed in 0.06s ===============================
"""

from docstring_parser.tests.test_epydoc import compose, parse

def test_compose():
    source = "Example source string"
    expected = "Expected output string"
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_compose _________________________________

    def test_compose():
        source = "Example source string"
        expected = "Expected output string"
>       assert compose(parse(source)) == expected
E       AssertionError: assert 'Example source string' == 'Expected output string'
E         
E         - Expected output string
E         + Example source string

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_valid_input.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_valid_input.py::test_compose
============================== 1 failed in 0.04s ===============================
"""
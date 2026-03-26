
import pytest
from docstring_parser.tests.test_numpydoc import parse, compose

@pytest.fixture(params=[
    ("\"\"\"This is a sample docstring.\nIt has multiple lines.\"\"\"", "This is a sample docstring.\nIt has multiple lines."),
    # Add more test cases as needed
])
def source_and_expected(request):
    return request.param

def test_compose(source_and_expected):
    source, expected = source_and_expected
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_2_test_edge_case.py F [100%]

=================================== FAILURES ===================================
______________________ test_compose[source_and_expected0] ______________________

source_and_expected = ('"""This is a sample docstring.\nIt has multiple lines."""', 'This is a sample docstring.\nIt has multiple lines.')

    def test_compose(source_and_expected):
        source, expected = source_and_expected
>       assert compose(parse(source)) == expected
E       assert '"""This is a...ple lines."""' == 'This is a sa...ltiple lines.'
E         
E         - This is a sample docstring.
E         + """This is a sample docstring.
E         ? +++
E         - It has multiple lines.
E         + It has multiple lines."""
E         ?                       +++

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_2_test_edge_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_compose_2_test_edge_case.py::test_compose[source_and_expected0]
============================== 1 failed in 0.05s ===============================
"""
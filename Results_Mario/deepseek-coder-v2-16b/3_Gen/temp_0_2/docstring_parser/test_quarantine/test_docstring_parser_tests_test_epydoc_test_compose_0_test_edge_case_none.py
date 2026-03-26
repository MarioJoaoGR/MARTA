
from docstring_parser.tests.test_epydoc import compose, parse

def test_compose_none():
    source = None
    expected = None
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
______________________________ test_compose_none _______________________________

    def test_compose_none():
        source = None
        expected = None
>       assert compose(parse(source)) == expected
E       AssertionError: assert '' == None
E        +  where '' = compose(<docstring_parser.common.Docstring object at 0x102bff790>)
E        +    where <docstring_parser.common.Docstring object at 0x102bff790> = parse(None)

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_edge_case_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_edge_case_none.py::test_compose_none
============================== 1 failed in 0.04s ===============================
"""
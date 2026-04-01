
import pytest
from docstring_parser.tests.test_epydoc import parse, compose, RenderingStyle

@pytest.fixture(params=[
    ("source1", "expected1"),
    ("source2", "expected2")
])
def source_and_expected(request):
    return request.param

def test_compose_clean(source_and_expected):
    source, expected = source_and_expected
    assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_edge_case_none.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________ test_compose_clean[source_and_expected0] ___________________

source_and_expected = ('source1', 'expected1')

    def test_compose_clean(source_and_expected):
        source, expected = source_and_expected
>       assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
E       AssertionError: assert 'source1' == 'expected1'
E         
E         - expected1
E         + source1

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_edge_case_none.py:14: AssertionError
___________________ test_compose_clean[source_and_expected1] ___________________

source_and_expected = ('source2', 'expected2')

    def test_compose_clean(source_and_expected):
        source, expected = source_and_expected
>       assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
E       AssertionError: assert 'source2' == 'expected2'
E         
E         - expected2
E         + source2

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_edge_case_none.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_edge_case_none.py::test_compose_clean[source_and_expected0]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_edge_case_none.py::test_compose_clean[source_and_expected1]
============================== 2 failed in 0.04s ===============================
"""
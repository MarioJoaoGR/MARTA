
import pytest
from docstring_parser.tests.test_epydoc import parse, compose, RenderingStyle

@pytest.fixture(params=[
    ("def func():  # Epydoc comment\n    '''This is a test'''\n", "This is a test"),
    ("class TestClass:\n    '''Class docstring'''", "Class docstring")
])
def source_expected_pairs(request):
    return request.param

def test_compose_clean(source_expected_pairs):
    source, expected = source_expected_pairs
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________ test_compose_clean[source_expected_pairs0] __________________

source_expected_pairs = ("def func():  # Epydoc comment\n    '''This is a test'''\n", 'This is a test')

    def test_compose_clean(source_expected_pairs):
        source, expected = source_expected_pairs
>       assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
E       assert "def func(): ... is a test'''" == 'This is a test'
E         
E         + def func():  # Epydoc comment
E         - This is a test
E         + '''This is a test'''
E         ? +++              +++

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_valid_input.py:14: AssertionError
__________________ test_compose_clean[source_expected_pairs1] __________________

source_expected_pairs = ("class TestClass:\n    '''Class docstring'''", 'Class docstring')

    def test_compose_clean(source_expected_pairs):
        source, expected = source_expected_pairs
>       assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
E       assert "class TestCl... docstring'''" == 'Class docstring'
E         
E         + class TestClass:
E         - Class docstring
E         + '''Class docstring'''
E         ? +++               +++

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_valid_input.py::test_compose_clean[source_expected_pairs0]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_clean_0_test_valid_input.py::test_compose_clean[source_expected_pairs1]
============================== 2 failed in 0.03s ===============================
"""
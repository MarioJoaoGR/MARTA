
import pytest
from docstring_parser.tests.test_epydoc import parse
from typing import Optional

@pytest.fixture(params=[None, "This is a test."])
def source(request):
    return request.param

@pytest.fixture(params=[None, "This is a test."])
def expected(request):
    return request.param

def test_short_description(source: Optional[str], expected: Optional[str]):
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_description_0_test_invalid_inputs.py . [ 25%]
FF.                                                                      [100%]

=================================== FAILURES ===================================
_________________ test_short_description[None-This is a test.] _________________

source = None, expected = 'This is a test.'

    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == 'This is a test.'
E        +  where None = <docstring_parser.common.Docstring object at 0x1069bfa00>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_description_0_test_invalid_inputs.py:17: AssertionError
_________________ test_short_description[This is a test.-None] _________________

source = 'This is a test.', expected = None

    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert 'This is a test.' == None
E        +  where 'This is a test.' = <docstring_parser.common.Docstring object at 0x1069e5d80>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_description_0_test_invalid_inputs.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_description_0_test_invalid_inputs.py::test_short_description[None-This is a test.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_description_0_test_invalid_inputs.py::test_short_description[This is a test.-None]
========================= 2 failed, 2 passed in 0.04s ==========================
"""
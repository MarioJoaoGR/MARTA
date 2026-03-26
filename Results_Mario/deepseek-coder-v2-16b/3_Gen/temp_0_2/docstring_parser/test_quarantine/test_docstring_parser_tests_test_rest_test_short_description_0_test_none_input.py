
import pytest
from docstring_parser.tests.test_rest import parse
import typing as T

@pytest.fixture(params=[None, ""])
def source(request):
    return request.param

@pytest.fixture(params=[None, ""])
def expected(request):
    return request.param

def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.description == expected
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_short_description_0_test_none_input.py . [ 25%]
F.F                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_short_description[None-] _________________________

source = None, expected = ''

    def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == ''
E        +  where None = <docstring_parser.common.Docstring object at 0x102724460>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_short_description_0_test_none_input.py:17: AssertionError
__________________________ test_short_description[-] ___________________________

source = '', expected = ''

    def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == ''
E        +  where None = <docstring_parser.common.Docstring object at 0x102727ac0>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_short_description_0_test_none_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_short_description_0_test_none_input.py::test_short_description[None-]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_short_description_0_test_none_input.py::test_short_description[-]
========================= 2 failed, 2 passed in 0.03s ==========================
"""
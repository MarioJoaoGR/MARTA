
import pytest
from docstring_parser.tests.test_google import parse
from typing import Optional

@pytest.fixture(params=[None, "", "def example(): ''' This is a summary. '''"])
def source(request):
    return request.param

@pytest.mark.parametrize("expected", [None, "This is a summary.", "Another summary."])
def test_short_description(source: Optional[str], expected: Optional[str]):
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    if expected is None:
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
collected 9 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py . [ 11%]
FF.FFFFF                                                                 [100%]

=================================== FAILURES ===================================
_______________ test_short_description[None-This is a summary.] ________________

source = None, expected = 'This is a summary.'

    @pytest.mark.parametrize("expected", [None, "This is a summary.", "Another summary."])
    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == 'This is a summary.'
E        +  where None = <docstring_parser.common.Docstring object at 0x102764670>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py:14: AssertionError
________________ test_short_description[None-Another summary.] _________________

source = None, expected = 'Another summary.'

    @pytest.mark.parametrize("expected", [None, "This is a summary.", "Another summary."])
    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == 'Another summary.'
E        +  where None = <docstring_parser.common.Docstring object at 0x102766bc0>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py:14: AssertionError
_________________ test_short_description[-This is a summary.] __________________

source = '', expected = 'This is a summary.'

    @pytest.mark.parametrize("expected", [None, "This is a summary.", "Another summary."])
    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == 'This is a summary.'
E        +  where None = <docstring_parser.common.Docstring object at 0x1027676d0>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py:14: AssertionError
__________________ test_short_description[-Another summary.] ___________________

source = '', expected = 'Another summary.'

    @pytest.mark.parametrize("expected", [None, "This is a summary.", "Another summary."])
    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == 'Another summary.'
E        +  where None = <docstring_parser.common.Docstring object at 0x102766080>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py:14: AssertionError
____ test_short_description[def example(): ''' This is a summary. '''-None] ____

source = "def example(): ''' This is a summary. '''", expected = None

    @pytest.mark.parametrize("expected", [None, "This is a summary.", "Another summary."])
    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       assert "def example(): ''' This is a summary. '''" == None
E        +  where "def example(): ''' This is a summary. '''" = <docstring_parser.common.Docstring object at 0x1027660e0>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py:14: AssertionError
_ test_short_description[def example(): ''' This is a summary. '''-This is a summary.] _

source = "def example(): ''' This is a summary. '''"
expected = 'This is a summary.'

    @pytest.mark.parametrize("expected", [None, "This is a summary.", "Another summary."])
    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       assert "def example(... summary. '''" == 'This is a summary.'
E         
E         - This is a summary.
E         + def example(): ''' This is a summary. '''

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py:14: AssertionError
_ test_short_description[def example(): ''' This is a summary. '''-Another summary.] _

source = "def example(): ''' This is a summary. '''"
expected = 'Another summary.'

    @pytest.mark.parametrize("expected", [None, "This is a summary.", "Another summary."])
    def test_short_description(source: Optional[str], expected: Optional[str]):
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       assert "def example(... summary. '''" == 'Another summary.'
E         
E         - Another summary.
E         + def example(): ''' This is a summary. '''

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py::test_short_description[None-This is a summary.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py::test_short_description[None-Another summary.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py::test_short_description[-This is a summary.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py::test_short_description[-Another summary.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py::test_short_description[def example(): ''' This is a summary. '''-None]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py::test_short_description[def example(): ''' This is a summary. '''-This is a summary.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_0_test_edge_case_none.py::test_short_description[def example(): ''' This is a summary. '''-Another summary.]
========================= 7 failed, 2 passed in 0.05s ==========================
"""
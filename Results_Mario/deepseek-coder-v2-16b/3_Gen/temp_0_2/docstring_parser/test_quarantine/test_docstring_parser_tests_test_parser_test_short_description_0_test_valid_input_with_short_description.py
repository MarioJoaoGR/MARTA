
import pytest
from docstring_parser.tests.test_parser import parse
import typing as T

@pytest.fixture(params=[None, ""])
def source(request):
    return request.param

@pytest.mark.parametrize("expected", [None, "", "This is a short description."])
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
collected 6 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py . [ 16%]
FF.FF                                                                    [100%]

=================================== FAILURES ===================================
________________________ test_short_description[None-] _________________________

source = None, expected = ''

    @pytest.mark.parametrize("expected", [None, "", "This is a short description."])
    def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == ''
E        +  where None = <docstring_parser.common.Docstring object at 0x101f8b070>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py:14: AssertionError
__________ test_short_description[None-This is a short description.] ___________

source = None, expected = 'This is a short description.'

    @pytest.mark.parametrize("expected", [None, "", "This is a short description."])
    def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == 'This is a short description.'
E        +  where None = <docstring_parser.common.Docstring object at 0x101f8bb20>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py:14: AssertionError
__________________________ test_short_description[-] ___________________________

source = '', expected = ''

    @pytest.mark.parametrize("expected", [None, "", "This is a short description."])
    def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == ''
E        +  where None = <docstring_parser.common.Docstring object at 0x101f8b550>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py:14: AssertionError
____________ test_short_description[-This is a short description.] _____________

source = '', expected = 'This is a short description.'

    @pytest.mark.parametrize("expected", [None, "", "This is a short description."])
    def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected
E       AssertionError: assert None == 'This is a short description.'
E        +  where None = <docstring_parser.common.Docstring object at 0x101ff0fd0>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py::test_short_description[None-]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py::test_short_description[None-This is a short description.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py::test_short_description[-]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parser_test_short_description_0_test_valid_input_with_short_description.py::test_short_description[-This is a short description.]
========================= 4 failed, 2 passed in 0.03s ==========================
"""
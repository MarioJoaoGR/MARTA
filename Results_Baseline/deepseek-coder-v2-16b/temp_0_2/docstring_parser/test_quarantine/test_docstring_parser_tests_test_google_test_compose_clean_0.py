
import pytest
from docstring_parser import parse, RenderingStyle
from docstring_parser.tests.test_google import test_compose_clean

# Test cases for the function `test_compose_clean`

def test_basic_usage():
    source = """
        Summary: This is a summary.
        Arguments: Details about arguments.
    """
    expected = "Summary: This is a summary.\nArguments: Details about arguments."
    test_compose_clean(source, expected)

def test_empty_docstring():
    source = ""
    expected = ""
    test_compose_clean(source, expected)

def test_complex_docstring():
    source = """
        Summary: This is a detailed summary.
        Multiple lines are supported.
        Arguments:
            - arg1: Description of argument 1.
            - arg2: Description of argument 2 with multiple details.
                - Nested detail 1
                - Nested detail 2
    """
    expected = "Summary: This is a detailed summary.\nMultiple lines are supported.\nArguments:\n    - arg1: Description of argument 1.\n    - arg2: Description of argument 2 with multiple details.\n        - Nested detail 1\n        - Nested detail 2"
    test_compose_clean(source, expected)

def test_different_rendering_style():
    source = """
        Summary: This is a summary.
        Arguments: Details about arguments.
    """
    expected = "Summary: This is a summary.\nArguments: Details about arguments."
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_0.py . [ 20%]
..F.                                                                     [100%]

=================================== FAILURES ===================================
____________________________ test_complex_docstring ____________________________

    def test_complex_docstring():
        source = """
            Summary: This is a detailed summary.
            Multiple lines are supported.
            Arguments:
                - arg1: Description of argument 1.
                - arg2: Description of argument 2 with multiple details.
                    - Nested detail 1
                    - Nested detail 2
        """
        expected = "Summary: This is a detailed summary.\nMultiple lines are supported.\nArguments:\n    - arg1: Description of argument 1.\n    - arg2: Description of argument 2 with multiple details.\n        - Nested detail 1\n        - Nested detail 2"
>       test_compose_clean(source, expected)

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_0.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = '\n        Summary: This is a detailed summary.\n        Multiple lines are supported.\n        Arguments:\n          ...ption of argument 2 with multiple details.\n                - Nested detail 1\n                - Nested detail 2\n    '
expected = 'Summary: This is a detailed summary.\nMultiple lines are supported.\nArguments:\n    - arg1: Description of argument 1.\n    - arg2: Description of argument 2 with multiple details.\n        - Nested detail 1\n        - Nested detail 2'

    @pytest.mark.parametrize(
        "source, expected",
        [
            (
                """
                Short description
    
                Args:
                    name: description 1
                    priority (int): description 2
                    sender (str, optional): description 3
                    message (str, optional): description 4, defaults to 'hello'
                    multiline (str?):
                        long description 5,
                            defaults to 'bye'
                """,
                "Short description\n"
                "\n"
                "Args:\n"
                "    name: description 1\n"
                "    priority (int): description 2\n"
                "    sender (str, optional): description 3\n"
                "    message (str, optional): description 4, defaults to 'hello'\n"
                "    multiline (str, optional): long description 5,\n"
                "        defaults to 'bye'",
            ),
        ],
    )
    def test_compose_clean(source: str, expected: str) -> None:
        """Test compose in clean mode."""
>       assert (
            compose(parse(source), rendering_style=RenderingStyle.CLEAN)
            == expected
        )
E       AssertionError: assert 'Summary: Thi...sted detail 2' == 'Summary: Thi...sted detail 2'
E         
E         Skipping 60 identical leading characters in diff, use -v to show
E           orted.
E         - Arguments:
E         + Args:
E               - arg1: Description of argument 1.
E               - arg2: Description of argument 2 with multiple details.
E                   - Nested detail 1
E                   - Nested detail 2

docstring_parser/docstring_parser/tests/test_google.py:959: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_0.py::test_complex_docstring
========================= 1 failed, 4 passed in 0.03s ==========================

"""
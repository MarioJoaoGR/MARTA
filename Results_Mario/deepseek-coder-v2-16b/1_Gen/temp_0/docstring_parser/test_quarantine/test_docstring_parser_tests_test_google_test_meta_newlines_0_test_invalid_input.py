
import pytest
from docstring_parser.tests.test_google import test_meta_newlines

def test_invalid_input():
    source = "This is not a docstring"
    with pytest.raises(ValueError):
        test_meta_newlines(source, None, None, False, False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 7 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_invalid_input.py . [ 14%]
.....F                                                                   [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        source = "This is not a docstring"
        with pytest.raises(ValueError):
>           test_meta_newlines(source, None, None, False, False)

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = 'This is not a docstring', expected_short_desc = None
expected_long_desc = None, expected_blank_short_desc = False
expected_blank_long_desc = False

    @pytest.mark.parametrize(
        "source, expected_short_desc, expected_long_desc, "
        "expected_blank_short_desc, expected_blank_long_desc",
        [
            (
                """
                Short description
                Args:
                    asd:
                """,
                "Short description",
                None,
                False,
                False,
            ),
            (
                """
                Short description
                Long description
                Args:
                    asd:
                """,
                "Short description",
                "Long description",
                False,
                False,
            ),
            (
                """
                Short description
                First line
                    Second line
                Args:
                    asd:
                """,
                "Short description",
                "First line\n    Second line",
                False,
                False,
            ),
            (
                """
                Short description
    
                First line
                    Second line
                Args:
                    asd:
                """,
                "Short description",
                "First line\n    Second line",
                True,
                False,
            ),
            (
                """
                Short description
    
                First line
                    Second line
    
                Args:
                    asd:
                """,
                "Short description",
                "First line\n    Second line",
                True,
                True,
            ),
            (
                """
                Args:
                    asd:
                """,
                None,
                None,
                False,
                False,
            ),
        ],
    )
    def test_meta_newlines(
        source: str,
        expected_short_desc: T.Optional[str],
        expected_long_desc: T.Optional[str],
        expected_blank_short_desc: bool,
        expected_blank_long_desc: bool,
    ) -> None:
        """Test parsing newlines around description sections."""
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert 'This is not a docstring' == None
E        +  where 'This is not a docstring' = <docstring_parser.common.Docstring object at 0x104795540>.short_description

docstring_parser/docstring_parser/tests/test_google.py:331: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_invalid_input.py::test_invalid_input
========================= 1 failed, 6 passed in 0.04s ==========================

"""
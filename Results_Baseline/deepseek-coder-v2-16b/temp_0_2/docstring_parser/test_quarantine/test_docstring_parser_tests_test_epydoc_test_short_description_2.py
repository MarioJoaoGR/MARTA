
import pytest
import typing as T
from docstring_parser import parse

# Test cases for short description parsing
@pytest.mark.parametrize(
    "source, expected",
    [
        (None, None),
        ("Short description here", "Short description here"),
        ("Another short description", "Another short description"),
        ("", None),
        # Additional test cases to cover different scenarios and edge cases
        ("Short description with newline\nand more text", "Short description with newline"),  # Test for multiline descriptions
        ("   Trimmed spaces   ", "Trimmed spaces"),  # Test for leading/trailing spaces trimming
        (None, None),  # Another test case to ensure it handles None correctly
    ],
)
def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    docstring = parse(source)
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_description_2.py . [ 14%]
....F.                                                                   [100%]

=================================== FAILURES ===================================
_________ test_short_description[   Trimmed spaces   -Trimmed spaces] __________

source = '   Trimmed spaces   ', expected = 'Trimmed spaces'

    @pytest.mark.parametrize(
        "source, expected",
        [
            (None, None),
            ("Short description here", "Short description here"),
            ("Another short description", "Another short description"),
            ("", None),
            # Additional test cases to cover different scenarios and edge cases
            ("Short description with newline\nand more text", "Short description with newline"),  # Test for multiline descriptions
            ("   Trimmed spaces   ", "Trimmed spaces"),  # Test for leading/trailing spaces trimming
            (None, None),  # Another test case to ensure it handles None correctly
        ],
    )
    def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
        """Test parsing short description."""
        docstring = parse(source)
>       assert docstring.short_description == expected, f"Expected {expected}, but got {docstring.short_description}"
E       AssertionError: Expected Trimmed spaces, but got Trimmed spaces   
E       assert 'Trimmed spaces   ' == 'Trimmed spaces'
E         
E         - Trimmed spaces
E         + Trimmed spaces   
E         ?               +++

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_description_2.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_description_2.py::test_short_description[   Trimmed spaces   -Trimmed spaces]
========================= 1 failed, 6 passed in 0.02s ==========================

"""
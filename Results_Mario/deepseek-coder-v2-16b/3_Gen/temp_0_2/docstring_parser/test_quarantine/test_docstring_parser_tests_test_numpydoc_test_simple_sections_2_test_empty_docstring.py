
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_empty_docstring() -> None:
    """Test parsing an empty docstring to check for proper error or warning message."""
    with pytest.raises(Exception):
        parse("")

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_simple_sections_2_test_empty_docstring.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_empty_docstring _____________________________

    def test_empty_docstring() -> None:
        """Test parsing an empty docstring to check for proper error or warning message."""
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_simple_sections_2_test_empty_docstring.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_simple_sections_2_test_empty_docstring.py::test_empty_docstring
============================== 1 failed in 0.03s ===============================
"""

import pytest
from docstring_parser.tests.test_epydoc import parse

def test_yields() -> None:
    """Test parsing yields."""
    # Test case for invalid annotation format
    with pytest.raises(ValueError):
        parse("Invalid docstring")

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_4_test_error_handling_invalid_annotation.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_yields __________________________________

    def test_yields() -> None:
        """Test parsing yields."""
        # Test case for invalid annotation format
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_4_test_error_handling_invalid_annotation.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_yields_4_test_error_handling_invalid_annotation.py::test_yields
============================== 1 failed in 0.03s ===============================
"""
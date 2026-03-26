
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_multiple_meta() -> None:
    """Test parsing multiple meta."""
    with pytest.raises(ValueError):
        # This should raise a ValueError because the expected format is not provided correctly in the docstring
        parse("Short description\n@meta1: asd\n    1\n        2\n    3")

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_multiple_meta_8_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_multiple_meta ______________________________

    def test_multiple_meta() -> None:
        """Test parsing multiple meta."""
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_multiple_meta_8_invalid_inputs.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_multiple_meta_8_invalid_inputs.py::test_multiple_meta
============================== 1 failed in 0.04s ===============================
"""
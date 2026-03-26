
from docstring_parser.tests.test_rest import parse
import pytest

def test_meta_with_multiline_description() -> None:
    """Test parsing multiline meta documentation."""
    with pytest.raises(Exception):  # Assuming a generic exception for invalid docstrings
        docstring = parse(
            """
            Short description

            :meta: asd
                1
                    2
                3
            """
        )

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_with_multiline_description_7_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________ test_meta_with_multiline_description _____________________

    def test_meta_with_multiline_description() -> None:
        """Test parsing multiline meta documentation."""
>       with pytest.raises(Exception):  # Assuming a generic exception for invalid docstrings
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_with_multiline_description_7_test_error_handling.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_with_multiline_description_7_test_error_handling.py::test_meta_with_multiline_description
============================== 1 failed in 0.04s ===============================
"""
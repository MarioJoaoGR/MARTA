
import pytest
from docstring_parser.tests.test_google import parse

def test_meta_with_multiline_description() -> None:
    """Test parsing multiline meta documentation."""
    with pytest.raises(Exception):  # Assuming a specific exception for invalid input in this context
        docstring = parse(
            """
            Short description

            Args:
                spam: asd
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_with_multiline_description_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_____________________ test_meta_with_multiline_description _____________________

    def test_meta_with_multiline_description() -> None:
        """Test parsing multiline meta documentation."""
>       with pytest.raises(Exception):  # Assuming a specific exception for invalid input in this context
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_with_multiline_description_2_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_with_multiline_description_2_test_invalid_input.py::test_meta_with_multiline_description
============================== 1 failed in 0.03s ===============================
"""
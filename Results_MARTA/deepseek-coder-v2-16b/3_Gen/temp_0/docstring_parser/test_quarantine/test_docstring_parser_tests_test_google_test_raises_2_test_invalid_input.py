
from docstring_parser.tests.test_google import parse
import pytest

def test_raises() -> None:
    """Test parsing raises in a Google-style docstring."""
    with pytest.raises(Exception):
        # This will raise an Exception if the parsing of raises does not work as expected.
        parse("""
        Short description
        Raises:
            ValueError: Description of the exception.
        """)

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_raises __________________________________

    def test_raises() -> None:
        """Test parsing raises in a Google-style docstring."""
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_2_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_2_test_invalid_input.py::test_raises
============================== 1 failed in 0.03s ===============================
"""
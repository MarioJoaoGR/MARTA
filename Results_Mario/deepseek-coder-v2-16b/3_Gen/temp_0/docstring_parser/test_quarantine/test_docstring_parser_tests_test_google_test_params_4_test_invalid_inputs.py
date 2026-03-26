
import pytest
from docstring_parser.tests.test_google import parse

def test_params() -> None:
    """Test parsing params."""
    with pytest.raises(AttributeError):  # Since googleparser does not exist, we mock it
        pass

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_params_4_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_params __________________________________

    def test_params() -> None:
        """Test parsing params."""
>       with pytest.raises(AttributeError):  # Since googleparser does not exist, we mock it
E       Failed: DID NOT RAISE <class 'AttributeError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_params_4_test_invalid_inputs.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_params_4_test_invalid_inputs.py::test_params
============================== 1 failed in 0.07s ===============================
"""
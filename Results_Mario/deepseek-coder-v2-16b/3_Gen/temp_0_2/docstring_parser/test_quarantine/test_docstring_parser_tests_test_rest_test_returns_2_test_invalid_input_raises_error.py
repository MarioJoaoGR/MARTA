
import pytest
from docstring_parser.tests.test_rest import parse

def test_invalid_input_raises_error():
    with pytest.raises(ValueError) as e:
        parse("Short description")
    assert str(e.value) == "Invalid docstring format"

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_returns_2_test_invalid_input_raises_error.py F [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_input_raises_error ________________________

    def test_invalid_input_raises_error():
>       with pytest.raises(ValueError) as e:
E       Failed: DID NOT RAISE <class 'ValueError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_returns_2_test_invalid_input_raises_error.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_returns_2_test_invalid_input_raises_error.py::test_invalid_input_raises_error
============================== 1 failed in 0.03s ===============================
"""
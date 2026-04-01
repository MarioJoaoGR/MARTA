
import pytest
from docstring_parser.tests.test_google import GoogleParser

def test_invalid_inputs():
    parser = GoogleParser()
    with pytest.raises(TypeError):
        parser.parse("""Test invalid input.""")

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_multi_line_parameter_type_4_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        parser = GoogleParser()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_multi_line_parameter_type_4_test_invalid_inputs.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_google_parser_multi_line_parameter_type_4_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""
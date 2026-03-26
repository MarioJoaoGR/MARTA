
import pytest
from docstring_parser.google import GoogleParser
from docstring_parser.common import ParseError

def test_error_handling():
    with pytest.raises(ParseError):
        parser = GoogleParser()
        parser.parse("")

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

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_1_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
>       with pytest.raises(ParseError):
E       Failed: DID NOT RAISE <class 'docstring_parser.common.ParseError'>

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_1_test_error_handling.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_parse_1_test_error_handling.py::test_error_handling
============================== 1 failed in 0.03s ===============================
"""
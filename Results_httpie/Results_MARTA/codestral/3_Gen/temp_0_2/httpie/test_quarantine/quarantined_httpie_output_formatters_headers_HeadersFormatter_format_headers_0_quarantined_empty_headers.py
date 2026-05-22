
import pytest
from unittest.mock import patch
from httpie.output.formatters.headers import HeadersFormatter

def test_empty_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = ""
    with patch('httpie.output.formatters.headers.HeadersFormatter.format_headers') as mock_format_headers:
        result = formatter.format_headers(headers)
        assert isinstance(result, str), "Expected a string output"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_empty_headers.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_headers ______________________________

    def test_empty_headers():
        formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
        headers = ""
        with patch('httpie.output.formatters.headers.HeadersFormatter.format_headers') as mock_format_headers:
            result = formatter.format_headers(headers)
>           assert isinstance(result, str), "Expected a string output"
E           AssertionError: Expected a string output
E           assert False
E            +  where False = isinstance(<MagicMock name='format_headers()' id='140606422343056'>, str)

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_empty_headers.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_empty_headers.py::test_empty_headers
============================== 1 failed in 0.08s ===============================
"""
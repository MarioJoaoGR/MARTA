
import pytest
from unittest.mock import patch
from httpie.output.formatters.headers import HeadersFormatter

def test_valid_headers():
    with patch('httpie.output.formatters.headers.HeadersFormatter', autospec=True) as MockHeadersFormatter:
        mock_instance = MockHeadersFormatter.return_value
        mock_instance.format_options = {'headers': {'sort': True}}

        result = mock_instance.format_headers("GET /example HTTP/1.1\nHost: example.com\nContent-Type: application/json\nUser-Agent: Mozilla/5.0")

        assert result == "GET /example HTTP/1.1\nContent-Type: application/json\nHost: example.com\nUser-Agent: Mozilla/5.0"

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

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_valid_headers.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_headers ______________________________

    def test_valid_headers():
        with patch('httpie.output.formatters.headers.HeadersFormatter', autospec=True) as MockHeadersFormatter:
            mock_instance = MockHeadersFormatter.return_value
            mock_instance.format_options = {'headers': {'sort': True}}
    
            result = mock_instance.format_headers("GET /example HTTP/1.1\nHost: example.com\nContent-Type: application/json\nUser-Agent: Mozilla/5.0")
    
>           assert result == "GET /example HTTP/1.1\nContent-Type: application/json\nHost: example.com\nUser-Agent: Mozilla/5.0"
E           AssertionError: assert <MagicMock name='HeadersFormatter().format_headers()' id='140011612431312'> == 'GET /example HTTP/1.1\nContent-Type: application/json\nHost: example.com\nUser-Agent: Mozilla/5.0'

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_valid_headers.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_valid_headers.py::test_valid_headers
============================== 1 failed in 0.06s ===============================
"""
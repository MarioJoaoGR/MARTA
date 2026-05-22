
import pytest
from unittest.mock import patch
from httpie.output.formatters.headers import HeadersFormatter

def test_valid_input():
    with patch('httpie.output.formatters.headers.HeadersFormatter.__init__', return_value=None):
        formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
        headers = "GET /example HTTP/1.1\nHost: example.com\nContent-Type: application/json\nUser-Agent: Mozilla/5.0"
        expected_output = "GET /example HTTP/1.1\nContent-Type: application/json\nHost: example.com\nUser-Agent: Mozilla/5.0"
        assert formatter.format_headers(headers) == expected_output

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('httpie.output.formatters.headers.HeadersFormatter.__init__', return_value=None):
            formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
            headers = "GET /example HTTP/1.1\nHost: example.com\nContent-Type: application/json\nUser-Agent: Mozilla/5.0"
            expected_output = "GET /example HTTP/1.1\nContent-Type: application/json\nHost: example.com\nUser-Agent: Mozilla/5.0"
>           assert formatter.format_headers(headers) == expected_output
E           AssertionError: assert 'GET /example...: Mozilla/5.0' == 'GET /example...: Mozilla/5.0'
E             
E             - GET /example HTTP/1.1
E             + GET /example HTTP/1.1
E             ?                      +
E             - Content-Type: application/json
E             + Content-Type: application/json
E             ?                               +...
E             
E             ...Full output truncated (4 lines hidden), use '-vv' to show

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_1_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.15s ===============================
"""
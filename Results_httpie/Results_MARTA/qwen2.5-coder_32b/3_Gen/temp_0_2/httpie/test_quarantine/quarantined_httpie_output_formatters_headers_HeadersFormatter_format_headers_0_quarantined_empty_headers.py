
import pytest
from unittest.mock import patch
from httpie.output.formatters.headers import HeadersFormatter

def test_empty_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    with patch('httpie.output.formatters.headers.HeadersFormatter.__init__', return_value=None):
        assert formatter.enabled is True
        headers = ""
        formatted_headers = formatter.format_headers(headers)
        expected_lines = ["GET /example HTTP/1.1"]
        assert formatted_headers.splitlines()[:len(expected_lines)] == expected_lines

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_empty_headers.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_headers ______________________________

    def test_empty_headers():
        formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
        with patch('httpie.output.formatters.headers.HeadersFormatter.__init__', return_value=None):
            assert formatter.enabled is True
            headers = ""
            formatted_headers = formatter.format_headers(headers)
            expected_lines = ["GET /example HTTP/1.1"]
>           assert formatted_headers.splitlines()[:len(expected_lines)] == expected_lines
E           AssertionError: assert [] == ['GET /example HTTP/1.1']
E             
E             Right contains one more item: 'GET /example HTTP/1.1'
E             Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_empty_headers.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_headers_HeadersFormatter_format_headers_0_test_empty_headers.py::test_empty_headers
============================== 1 failed in 0.09s ===============================
"""
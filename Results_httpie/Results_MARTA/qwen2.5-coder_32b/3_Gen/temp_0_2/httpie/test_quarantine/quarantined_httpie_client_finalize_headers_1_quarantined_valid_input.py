
import pytest
from unittest.mock import patch
from httpie.client import HTTPHeadersDict, finalize_headers

class TestFinalizeHeaders:
    def test_valid_input(self):
        headers = HTTPHeadersDict()
        headers.add('Content-Type', 'application/json')
        headers.add('Set-Cookie', 'cookie1=value1;')
        headers.add('Cache-Control', None)
    
        with patch('httpie.client.HTTPHeadersDict') as mock_headers:
            mock_headers.return_value = HTTPHeadersDict()
            finalized_headers = finalize_headers(headers)
    
            assert finalized_headers == headers, f"Expected {headers}, but got {finalized_headers}"

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_finalize_headers_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_____________________ TestFinalizeHeaders.test_valid_input _____________________

self = <test_httpie_client_finalize_headers_1_test_valid_input.TestFinalizeHeaders object at 0x7f86c193af50>

    def test_valid_input(self):
        headers = HTTPHeadersDict()
        headers.add('Content-Type', 'application/json')
        headers.add('Set-Cookie', 'cookie1=value1;')
        headers.add('Cache-Control', None)
    
        with patch('httpie.client.HTTPHeadersDict') as mock_headers:
            mock_headers.return_value = HTTPHeadersDict()
            finalized_headers = finalize_headers(headers)
    
>           assert finalized_headers == headers, f"Expected {headers}, but got {finalized_headers}"
E           AssertionError: Expected <HTTPHeadersDict('Content-Type': 'application/json', 'Set-Cookie': 'cookie1=value1;', 'Cache-Control': None)>, but got <HTTPHeadersDict('Content-Type': b'application/json', 'Set-Cookie': b'cookie1=value1;', 'Cache-Control': None)>
E           assert <HTTPHeadersD...ntrol': None)> == <HTTPHeadersD...ntrol': None)>
E             
E             Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_finalize_headers_1_test_valid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_finalize_headers_1_test_valid_input.py::TestFinalizeHeaders::test_valid_input
============================== 1 failed in 0.27s ===============================
"""

import requests
from unittest.mock import patch
from httpie.client import transform_headers

def test_valid_input():
    request = requests.Request('GET', 'http://example.com')
    prepared_request = request.prepare()
    prepared_request.headers['Content-Length'] = '0'
    
    with patch('requests.Request.prepare', return_value=prepared_request):
        transform_headers(request, prepared_request)
    
    assert 'Content-Length' not in prepared_request.headers

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

httpie/Test4DT_tests_codestral/test_httpie_client_transform_headers_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        request = requests.Request('GET', 'http://example.com')
        prepared_request = request.prepare()
        prepared_request.headers['Content-Length'] = '0'
    
        with patch('requests.Request.prepare', return_value=prepared_request):
            transform_headers(request, prepared_request)
    
>       assert 'Content-Length' not in prepared_request.headers
E       AssertionError: assert 'Content-Length' not in <HTTPHeadersDict('Content-Length': '0')>
E        +  where <HTTPHeadersDict('Content-Length': '0')> = <PreparedRequest [GET]>.headers

httpie/Test4DT_tests_codestral/test_httpie_client_transform_headers_1_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_client_transform_headers_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.26s ===============================
"""
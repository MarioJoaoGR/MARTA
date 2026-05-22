
import requests
from unittest.mock import patch
from httpie.client import IGNORE_CONTENT_LENGTH_METHODS, transform_headers

def test_edge_case():
    with patch('httpie.client.IGNORE_CONTENT_LENGTH_METHODS', {'GET', 'HEAD'}):
        request = requests.Request(method='POST', url='http://example.com')
        prepared_request = requests.PreparedRequest()
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

httpie/Test4DT_tests_codestral/test_httpie_client_transform_headers_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with patch('httpie.client.IGNORE_CONTENT_LENGTH_METHODS', {'GET', 'HEAD'}):
            request = requests.Request(method='POST', url='http://example.com')
            prepared_request = requests.PreparedRequest()
>           transform_headers(request, prepared_request)

httpie/Test4DT_tests_codestral/test_httpie_client_transform_headers_1_test_edge_case.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/client.py:227: in transform_headers
    apply_missing_repeated_headers(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

original_headers = {}, prepared_request = <PreparedRequest [None]>

    def apply_missing_repeated_headers(
        original_headers: HTTPHeadersDict,
        prepared_request: requests.PreparedRequest
    ) -> None:
        """Update the given `prepared_request`'s headers with the original
        ones. This allows the requests to be prepared as usual, and then later
        merged with headers that are specified multiple times."""
    
>       new_headers = HTTPHeadersDict(prepared_request.headers)
E       TypeError: 'NoneType' object is not iterable

httpie/httpie/client.py:241: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_client_transform_headers_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.27s ===============================
"""
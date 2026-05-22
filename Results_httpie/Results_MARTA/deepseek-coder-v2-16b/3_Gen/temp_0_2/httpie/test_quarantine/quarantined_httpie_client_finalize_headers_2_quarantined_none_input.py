
import pytest
from unittest.mock import patch
from httpie.client import HTTPHeadersDict, finalize_headers

def test_none_input():
    headers = HTTPHeadersDict()
    with patch('httpie.client.HTTPHeadersDict', return_value=headers):
        # Add a header with None value
        headers.add('Content-Type', None)

        # Call the function under test
        finalized_headers = finalize_headers(headers)

        # Assert that the 'Content-Type' header is not present in the final headers
        assert 'Content-Type' not in finalized_headers

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_finalize_headers_2_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        headers = HTTPHeadersDict()
        with patch('httpie.client.HTTPHeadersDict', return_value=headers):
            # Add a header with None value
            headers.add('Content-Type', None)
    
            # Call the function under test
>           finalized_headers = finalize_headers(headers)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_finalize_headers_2_test_none_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

headers = <HTTPHeadersDict('Content-Type': None)>

    def finalize_headers(headers: HTTPHeadersDict) -> HTTPHeadersDict:
        final_headers = HTTPHeadersDict()
>       for name, value in headers.items():
E       RuntimeError: MultiDict is changed during iteration

httpie/httpie/client.py:194: RuntimeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_finalize_headers_2_test_none_input.py::test_none_input
============================== 1 failed in 0.29s ===============================
"""
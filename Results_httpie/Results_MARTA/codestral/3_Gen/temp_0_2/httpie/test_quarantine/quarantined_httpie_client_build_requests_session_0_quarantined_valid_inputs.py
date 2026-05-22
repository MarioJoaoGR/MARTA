
import pytest
from unittest.mock import patch
import requests
from httpie.client import build_requests_session, HTTPieHTTPAdapter, HTTPieHTTPSAdapter

def test_valid_inputs():
    with patch('httpie.client.HTTPieHTTPSAdapter') as mock_adapter:
        session = build_requests_session(verify=True)

        assert isinstance(session, requests.Session)
        assert len(session.adapters) == 2
        assert 'http://' in session.adapters
        assert 'https://' in session.adapters

        http_adapter = session.adapters['http://']
        https_adapter = session.adapters['https://']

        assert isinstance(http_adapter, requests.adapters.HTTPAdapter)
        assert isinstance(https_adapter, mock_adapter)

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

httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('httpie.client.HTTPieHTTPSAdapter') as mock_adapter:
            session = build_requests_session(verify=True)
    
            assert isinstance(session, requests.Session)
            assert len(session.adapters) == 2
            assert 'http://' in session.adapters
            assert 'https://' in session.adapters
    
            http_adapter = session.adapters['http://']
            https_adapter = session.adapters['https://']
    
            assert isinstance(http_adapter, requests.adapters.HTTPAdapter)
>           assert isinstance(https_adapter, mock_adapter)
E           TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_0_test_valid_inputs.py:20: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.17s ===============================
"""
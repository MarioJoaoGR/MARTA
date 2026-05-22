
import requests
from unittest.mock import patch, MagicMock
from httpie.client import build_requests_session

def test_build_requests_session():
    with patch('httpie.client.HTTPieHTTPSAdapter') as mock_adapter:
        session = build_requests_session(verify=True)
        
        assert isinstance(session, requests.Session)
        assert len(session.adapters) == 2
        assert 'http://' in session.adapters
        assert 'https://' in session.adapters
        
        http_adapter = session.adapters['http://']
        https_adapter = session.adapters['https://']
        
        assert isinstance(http_adapter, requests.adapters.HTTPAdapter)
        assert isinstance(https_adapter, MagicMock)
        assert https_adapter.called

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

httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_________________________ test_build_requests_session __________________________

    def test_build_requests_session():
        with patch('httpie.client.HTTPieHTTPSAdapter') as mock_adapter:
            session = build_requests_session(verify=True)
    
            assert isinstance(session, requests.Session)
            assert len(session.adapters) == 2
            assert 'http://' in session.adapters
            assert 'https://' in session.adapters
    
            http_adapter = session.adapters['http://']
            https_adapter = session.adapters['https://']
    
            assert isinstance(http_adapter, requests.adapters.HTTPAdapter)
            assert isinstance(https_adapter, MagicMock)
>           assert https_adapter.called
E           AssertionError: assert False
E            +  where False = <MagicMock name='HTTPieHTTPSAdapter()' id='139859798687056'>.called

httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_1_test_edge_cases.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_1_test_edge_cases.py::test_build_requests_session
============================== 1 failed in 0.22s ===============================
"""
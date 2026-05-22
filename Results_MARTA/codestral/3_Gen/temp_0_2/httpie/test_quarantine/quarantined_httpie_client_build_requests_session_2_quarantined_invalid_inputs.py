
import pytest
from unittest.mock import patch, MagicMock
from httpie.client import build_requests_session
import requests

def test_invalid_inputs():
    with patch('httpie.client.HTTPieHTTPSAdapter', autospec=True) as mock_adapter:
        session = requests.Session()
        custom_session = build_requests_session(verify=False, ssl_version='TLSv1', ciphers='DEFAULT')
        
        # Add assertions to verify the expected behavior after fixing the error
        assert isinstance(custom_session, requests.Session)
        assert hasattr(custom_session, 'mount')
        mock_adapter.assert_called_once_with(ciphers='DEFAULT', verify=False, ssl_version='TLSv1')

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

httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('httpie.client.HTTPieHTTPSAdapter', autospec=True) as mock_adapter:
            session = requests.Session()
>           custom_session = build_requests_session(verify=False, ssl_version='TLSv1', ciphers='DEFAULT')

httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_2_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

verify = False, ssl_version = 'TLSv1', ciphers = 'DEFAULT'

    def build_requests_session(
        verify: bool,
        ssl_version: str = None,
        ciphers: str = None,
    ) -> requests.Session:
        requests_session = requests.Session()
    
        # Install our adapter.
        http_adapter = HTTPieHTTPAdapter()
        https_adapter = HTTPieHTTPSAdapter(
            ciphers=ciphers,
            verify=verify,
            ssl_version=(
>               AVAILABLE_SSL_VERSION_ARG_MAPPING[ssl_version]
                if ssl_version else None
            ),
        )
E       KeyError: 'TLSv1'

httpie/httpie/client.py:169: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_client_build_requests_session_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.29s ===============================
"""
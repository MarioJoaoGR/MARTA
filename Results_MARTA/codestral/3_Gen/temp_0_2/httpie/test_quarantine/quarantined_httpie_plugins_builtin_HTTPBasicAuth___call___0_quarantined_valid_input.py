
import pytest
from unittest.mock import patch
from httpie.plugins.builtin import HTTPBasicAuth
import requests

def test_valid_input():
    with patch('httpie.plugins.builtin.HTTPBasicAuth.make_header') as mock_make_header:
        mock_make_header.return_value = b'Basic dXNlcm5hbWU6cGFzc3dvcmQ='

        setup_auth = HTTPBasicAuth('username', 'password')
        request = requests.PreparedRequest()
        request.url = 'http://example.com'

        auth = setup_auth(request)

        assert 'Authorization' in request.headers
        assert request.headers['Authorization'] == b'Basic dXNlcm5hbWU6cGFzc3dvcmQ='

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

httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth___call___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('httpie.plugins.builtin.HTTPBasicAuth.make_header') as mock_make_header:
            mock_make_header.return_value = b'Basic dXNlcm5hbWU6cGFzc3dvcmQ='
    
            setup_auth = HTTPBasicAuth('username', 'password')
            request = requests.PreparedRequest()
            request.url = 'http://example.com'
    
>           auth = setup_auth(request)

httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth___call___0_test_valid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.plugins.builtin.HTTPBasicAuth object at 0x7fcd6a04c290>
request = <PreparedRequest [None]>

    def __call__(
        self,
        request: requests.PreparedRequest
    ) -> requests.PreparedRequest:
        """
        Override username/password serialization to allow unicode.
    
        See https://github.com/httpie/cli/issues/212
    
        """
        # noinspection PyTypeChecker
        request.headers['Authorization'] = type(self).make_header(
>           self.username, self.password).encode('latin1')
E       AttributeError: 'bytes' object has no attribute 'encode'

httpie/httpie/plugins/builtin.py:27: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth___call___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""
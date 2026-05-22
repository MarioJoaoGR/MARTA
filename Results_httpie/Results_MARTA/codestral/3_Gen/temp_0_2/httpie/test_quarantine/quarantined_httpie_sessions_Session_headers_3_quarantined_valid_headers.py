
from httpie.sessions import Session, Environment, HTTPHeadersDict
from unittest.mock import patch
import pytest

class TestSessionHeaders:
    @patch('httpie.sessions.HTTPHeadersDict')
    def test_valid_headers(self, mock_headers):
        # Arrange
        session = Session(path='session_file', env=Environment(), bound_host='example.com', session_id='12345')
    
        # Act
        headers = session.headers()
    
        # Assert
        assert mock_headers.return_value == headers, f"Expected {mock_headers.return_value}, but got {headers}"

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

httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_headers_3_test_valid_headers.py F [100%]

=================================== FAILURES ===================================
____________________ TestSessionHeaders.test_valid_headers _____________________

self = <Test4DT_tests_codestral.test_httpie_sessions_Session_headers_3_test_valid_headers.TestSessionHeaders object at 0x7f3fc5790290>
mock_headers = <MagicMock name='HTTPHeadersDict' id='139911872715472'>

    @patch('httpie.sessions.HTTPHeadersDict')
    def test_valid_headers(self, mock_headers):
        # Arrange
        session = Session(path='session_file', env=Environment(), bound_host='example.com', session_id='12345')
    
        # Act
        headers = session.headers()
    
        # Assert
>       assert mock_headers.return_value == headers, f"Expected {mock_headers.return_value}, but got {headers}"
E       AssertionError: Expected <MagicMock name='HTTPHeadersDict()' id='139911872724304'>, but got <MagicMock name='HTTPHeadersDict().copy()()' id='139911872773072'>
E       assert <MagicMock na...911872724304'> == <MagicMock na...911872773072'>
E         
E         Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_headers_3_test_valid_headers.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_headers_3_test_valid_headers.py::TestSessionHeaders::test_valid_headers
============================== 1 failed in 0.23s ===============================
"""
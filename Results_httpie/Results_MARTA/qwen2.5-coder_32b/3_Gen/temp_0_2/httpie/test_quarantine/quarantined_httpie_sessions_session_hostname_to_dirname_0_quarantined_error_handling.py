
import os
from unittest import TestCase, mock
from httpie.sessions import session_hostname_to_dirname

class TestSessionHostnameToDirname(TestCase):
    @mock.patch('httpie.sessions.SESSIONS_DIR_NAME', '/path/to/sessions')
    def test_session_hostname_to_dirname(self):
        # Test case with hostname without port
        result = session_hostname_to_dirname('example.com', 'session1')
        expected_output = os.path.join('/path/to/sessions', 'example_com', 'session1.json')
        self.assertEqual(result, expected_output)
        
        # Test case with hostname containing port
        result = session_hostname_to_dirname('example.com:8080', 'session2')
        expected_output = os.path.join('/path/to/sessions', 'example_com_8080', 'session2.json')
        self.assertEqual(result, expected_output)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_session_hostname_to_dirname_0_test_error_handling.py F [100%]

=================================== FAILURES ===================================
________ TestSessionHostnameToDirname.test_session_hostname_to_dirname _________

self = <test_httpie_sessions_session_hostname_to_dirname_0_test_error_handling.TestSessionHostnameToDirname testMethod=test_session_hostname_to_dirname>

    @mock.patch('httpie.sessions.SESSIONS_DIR_NAME', '/path/to/sessions')
    def test_session_hostname_to_dirname(self):
        # Test case with hostname without port
        result = session_hostname_to_dirname('example.com', 'session1')
        expected_output = os.path.join('/path/to/sessions', 'example_com', 'session1.json')
>       self.assertEqual(result, expected_output)
E       AssertionError: '/path/to/sessions/example.com/session1.json' != '/path/to/sessions/example_com/session1.json'
E       - /path/to/sessions/example.com/session1.json
E       ?                          ^
E       + /path/to/sessions/example_com/session1.json
E       ?                          ^

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_session_hostname_to_dirname_0_test_error_handling.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_session_hostname_to_dirname_0_test_error_handling.py::TestSessionHostnameToDirname::test_session_hostname_to_dirname
============================== 1 failed in 0.26s ===============================
"""
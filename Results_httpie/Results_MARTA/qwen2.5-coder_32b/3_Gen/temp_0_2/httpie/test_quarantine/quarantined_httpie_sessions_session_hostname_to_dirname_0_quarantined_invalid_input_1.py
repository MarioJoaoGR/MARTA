
import os
from unittest import TestCase, mock
from httpie.sessions import SESSIONS_DIR_NAME

class TestSessionHostnameToDirname(TestCase):
    @mock.patch('httpie.sessions.SESSIONS_DIR_NAME', None)
    def test_invalid_input_1(self):
        with self.assertRaises(NameError):
            session_hostname_to_dirname('example.com:8080', 'session2')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_sessions_session_hostname_to_dirname_0_test_invalid_input_1
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_session_hostname_to_dirname_0_test_invalid_input_1.py:10:12: E0602: Undefined variable 'session_hostname_to_dirname' (undefined-variable)


"""
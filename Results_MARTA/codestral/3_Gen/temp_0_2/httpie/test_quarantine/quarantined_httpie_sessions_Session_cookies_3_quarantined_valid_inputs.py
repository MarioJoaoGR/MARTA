
import unittest
from unittest.mock import patch, MagicMock
from httpie.sessions import Session
from httpie.sessions.compat import HTTPHeadersDict
from requests_toolbelt.cookies import RequestsCookieJar
from httpie.sessions import Environment

class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session(
            path="path/to/session_file",
            env=Environment(),
            bound_host="example.com",
            session_id="unique_session_id"
        )
        self.session['headers'] = ['Authorization: Bearer token123']

    @patch('httpie.sessions.compat.HTTPHeadersDict')
    def test_valid_inputs(self, MockHTTPHeadersDict):
        # Arrange
        mock_cookie_jar = MagicMock()
        self.session._headers = MockHTTPHeadersDict.return_value
        self.session.cookie_jar = mock_cookie_jar

        # Act
        cookies = self.session.cookies()

        # Assert
        MockHTTPHeadersDict.assert_called_once()
        mock_cookie_jar.clear_expired_cookies.assert_called_once()
        self.assertEqual(cookies, mock_cookie_jar)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_sessions_Session_cookies_3_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_cookies_3_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.sessions.compat' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_cookies_3_test_valid_inputs.py:5:0: E0611: No name 'compat' in module 'httpie.sessions' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_cookies_3_test_valid_inputs.py:6:0: E0611: No name 'RequestsCookieJar' in module 'requests_toolbelt.cookies' (no-name-in-module)


"""
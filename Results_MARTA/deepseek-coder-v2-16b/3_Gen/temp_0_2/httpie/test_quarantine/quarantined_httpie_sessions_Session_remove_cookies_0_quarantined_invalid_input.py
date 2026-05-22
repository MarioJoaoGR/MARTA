
from httpie.sessions import remove_cookie_by_name
from unittest.mock import patch

class TestSessionRemoveCookies(unittest.TestCase):
    @patch('httpie.sessions.remove_cookie_by_name')
    def test_remove_cookies(self, mock_remove_cookie):
        cookies_to_remove = [{'name': 'cookie1'}, {'name': 'cookie2'}]
        session = Session(path='dummy', env=Environment(), bound_host='example.com', session_id='session1')
        session.remove_cookies(cookies_to_remove)
    
        # Assert that remove_cookie_by_name was called twice with the correct arguments
        mock_remove_cookie.assert_any_call(session.cookie_jar, 'cookie1', domain='example.com', path='/')
        mock_remove_cookie.assert_any_call(session.cookie_jar, 'cookie2', domain='example.com', path='/')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_sessions_Session_remove_cookies_0_test_invalid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_remove_cookies_0_test_invalid_input.py:5:31: E0602: Undefined variable 'unittest' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_remove_cookies_0_test_invalid_input.py:9:18: E0602: Undefined variable 'Session' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_remove_cookies_0_test_invalid_input.py:9:44: E0602: Undefined variable 'Environment' (undefined-variable)


"""
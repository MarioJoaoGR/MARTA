
import pytest
from httpie.sessions import Session, RequestsCookieJar
from unittest.mock import patch
from typing import List, Dict, Any

class TestSessionAddCookies:
    @patch('httpie.sessions.RequestsCookieJar')
    def test_add_cookies(self, mock_cookiejar):
        # Create a session instance with mocked cookie jar
        session = Session(path='dummy_path', env=None, bound_host='example.com', session_id='12345')
        
        # Define cookies with an explicit None domain for testing
        cookies = [{'name': 'user_cookie', 'value': 'user_value', 'domain': None}]
        
        # Call the method under test
        session._add_cookies(cookies)
        
        # Assert that the cookie is added to the cookie jar with an empty string domain
        expected_domain = '' if cookies[0]['domain'] is None else cookies[0]['domain']
        assert len(session.cookie_jar.set.call_args_list) == 1
        call_args = session.cookie_jar.set.call_args_list[0][1]
        assert call_args['domain'] == expected_domain

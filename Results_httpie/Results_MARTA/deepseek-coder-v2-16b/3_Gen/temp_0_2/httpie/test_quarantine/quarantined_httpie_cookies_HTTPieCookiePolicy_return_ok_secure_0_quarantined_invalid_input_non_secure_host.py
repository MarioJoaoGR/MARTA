
import unittest
from httpie.cookies import HTTPieCookiePolicy
from httpie.models import HttpRequest
from urllib import parse

class TestHTTPieCookiePolicy(unittest.TestCase):
    
    def setUp(self):
        self.policy = HTTPieCookiePolicy()
    
    def test_invalid_input_non_secure_host(self):
        with unittest.mock.patch('httpie.cookies.HTTPieCookiePolicy._is_local_host', return_value=True):
            request = HttpRequest('http://example.com')
            cookie = 'some_cookie'
            result = self.policy.return_ok_secure(cookie, request)
            self.assertTrue(result)
            
            request = HttpRequest('https://example.com')
            cookie = 'another_cookie'
            result = self.policy.return_ok_secure(cookie, request)
            self.assertTrue(result)
            
            request = HttpRequest('http://localhost:8080')
            cookie = 'third_cookie'
            result = self.policy.return_ok_secure(cookie, request)
            self.assertTrue(result)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cookies_HTTPieCookiePolicy_return_ok_secure_0_test_invalid_input_non_secure_host
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cookies_HTTPieCookiePolicy_return_ok_secure_0_test_invalid_input_non_secure_host.py:4:0: E0611: No name 'HttpRequest' in module 'httpie.models' (no-name-in-module)


"""

import unittest
from httpie.cookies import HTTPieCookiePolicy
from httpie.models import HttpRequest
from urllib import parse

class TestHTTPieCookiePolicy(unittest.TestCase):
    
    def setUp(self):
        self.policy = HTTPieCookiePolicy()
    
    def test_return_ok_secure_with_secure_protocol(self):
        request = HttpRequest('https://example.com')
        cookie = 'some_cookie'
        result = self.policy.return_ok_secure(cookie, request)
        self.assertTrue(result)
    
    def test_return_ok_secure_with_local_host(self):
        request = HttpRequest('http://localhost:8080')
        cookie = 'another_cookie'
        result = self.policy.return_ok_secure(cookie, request)
        self.assertTrue(result)
    
    def test_return_ok_secure_with_non_secure_host(self):
        request = HttpRequest('http://example.com')
        cookie = 'third_cookie'
        result = self.policy.return_ok_secure(cookie, request)
        self.assertFalse(result)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cookies_HTTPieCookiePolicy_return_ok_secure_0_test_valid_input_secure_protocol
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cookies_HTTPieCookiePolicy_return_ok_secure_0_test_valid_input_secure_protocol.py:4:0: E0611: No name 'HttpRequest' in module 'httpie.models' (no-name-in-module)


"""
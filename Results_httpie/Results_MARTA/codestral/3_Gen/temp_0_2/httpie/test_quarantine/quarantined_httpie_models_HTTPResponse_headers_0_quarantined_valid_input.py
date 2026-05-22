
import unittest
from httpie.models import HTTPResponse
from unittest.mock import patch

class TestHTTPResponseHeaders(unittest.TestCase):
    @patch('httpie.models.HTTPResponse._orig', autospec=True)
    def test_valid_input(self, mock_orig):
        # Mocking the original response object
        mock_orig.status_code = 200
        mock_orig.reason = 'OK'
        mock_orig.headers = {
            'Content-Type': 'text/html; charset=utf-8',
            'Set-Cookie': ['cookie1=value1', 'cookie2=value2']
        }
        
        response = HTTPResponse()
        result = response.headers()
        
        expected_output = (
            f'HTTP/{response.version} 200 OK\r\n'
            f'Content-Type: text/html; charset=utf-8\r\n'
            f'Set-Cookie: cookie1=value1\r\n'
            f'Set-Cookie: cookie2=value2'
        )
        
        self.assertEqual(result, expected_output)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPResponse_headers_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPResponse_headers_0_test_valid_input.py:17:19: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPResponse_headers_0_test_valid_input.py:18:17: E1102: response.headers is not callable (not-callable)


"""
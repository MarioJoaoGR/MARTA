
import pytest
from unittest.mock import patch
from httpie.models import HTTPResponse

def split_cookies(value):
    return value.split(';')

class TestHTTPResponseHeaders:
    
    @pytest.fixture
    def setup_response(self):
        response = HTTPResponse()
        response._orig = type('OriginalResponse', (object,), {
            'status_code': 200,
            'reason': 'OK',
            'headers': {
                'Content-Type': 'text/html; charset=utf-8',
                'Set-Cookie': 'cookie1=value1; cookie2=value2'
            }
        })()
        return response
    
    @patch('httpie.models.HTTPResponse.split_cookies', side_effect=lambda value: [value])
    def test_invalid_input(self, mock_split_cookies, setup_response):
        response = setup_response
        assert isinstance(response.headers(), str)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_models_HTTPResponse_headers_0_test_invalid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPResponse_headers_0_test_invalid_input.py:13:19: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
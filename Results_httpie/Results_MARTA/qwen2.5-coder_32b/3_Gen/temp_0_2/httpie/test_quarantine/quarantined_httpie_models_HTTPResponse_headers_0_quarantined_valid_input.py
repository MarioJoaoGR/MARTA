
import pytest
from unittest.mock import patch
from httpie.models import HTTPResponse

@pytest.fixture
def valid_http_response():
    response = HTTPResponse()
    response._orig = type('OriginalResponse', (object,), {
        'status_code': 200,
        'reason': 'OK',
        'headers': {
            'Content-Type': 'text/html; charset=utf-8',
            'Set-Cookie': ['cookie1=value1', 'cookie2=value2']
        }
    })()
    return response

def test_valid_input(valid_http_response):
    with patch('httpie.models.HTTPResponse._orig', valid_http_response._orig):
        assert valid_http_response.headers() == (
            'HTTP/1.1 200 OK\r\n'
            'Content-Type: text/html; charset=utf-8\r\n'
            'Set-Cookie: cookie1=value1\r\n'
            'Set-Cookie: cookie2=value2'
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPResponse_headers_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPResponse_headers_0_test_valid_input.py:8:15: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
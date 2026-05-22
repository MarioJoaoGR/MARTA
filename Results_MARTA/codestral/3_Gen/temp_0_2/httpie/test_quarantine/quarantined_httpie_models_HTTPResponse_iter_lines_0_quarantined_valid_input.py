
import pytest
from unittest.mock import patch
from httpie.models import HTTPResponse

def test_iter_lines():
    # Create a mock instance of requests.models.Response
    class MockResponse:
        def iter_lines(self, chunk_size):
            return [b'line1', b'line2', b'line3']  # Example lines for testing

    http_response = HTTPResponse()
    with patch('httpie.models.HTTPResponse._orig', MockResponse()):
        result = list(http_response.iter_lines(chunk_size=1024))
    
    expected_result = [(b'line1', b'\n'), (b'line2', b'\n'), (b'line3', b'\n')]
    assert result == expected_result

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPResponse_iter_lines_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPResponse_iter_lines_0_test_valid_input.py:12:20: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
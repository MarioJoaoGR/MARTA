
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPResponse

@pytest.fixture
def valid_http_response():
    response = MagicMock()
    return HTTPResponse(response=response)

def test_valid_input(valid_http_response):
    with patch('httpie.models.HTTPResponse._orig.iter_content') as mock_iter_content:
        chunk_size = 512
        valid_http_response.iter_body(chunk_size=chunk_size)
        mock_iter_content.assert_called_once_with(chunk_size=chunk_size)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPResponse_iter_body_1_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPResponse_iter_body_1_test_valid_input.py:9:11: E1123: Unexpected keyword argument 'response' in constructor call (unexpected-keyword-arg)
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPResponse_iter_body_1_test_valid_input.py:9:11: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
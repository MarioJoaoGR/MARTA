
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPRequest

@pytest.fixture
def setup_http_request():
    # Create a mock requests.models.Response object
    response = MagicMock()
    response.body = b"test body"
    
    # Create an instance of HTTPRequest with the mocked response
    http_request = HTTPRequest()
    http_request.response = response
    return http_request, response

def test_iter_body(setup_http_request):
    http_request, _ = setup_http_request
    
    # Test iterating over the body with a chunk size of 5
    chunks = list(http_request.iter_body(chunk_size=5))
    
    assert len(chunks) == 2
    assert chunks[0] == b"test "
    assert chunks[1] == b"body"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPRequest_iter_body_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPRequest_iter_body_0_test_edge_case.py:13:19: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
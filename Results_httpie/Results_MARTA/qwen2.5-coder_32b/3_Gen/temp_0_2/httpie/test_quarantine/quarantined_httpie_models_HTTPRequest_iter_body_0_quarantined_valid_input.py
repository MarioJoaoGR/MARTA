
import pytest
from httpie.models import HTTPRequest

@pytest.fixture
def valid_request():
    # Create a mock requests.models.Request object for testing
    req = HTTPRequest()
    req.body = b"test body"
    return req

def test_iter_body(valid_request):
    chunk_size = 5
    chunks = list(valid_request.iter_body(chunk_size))
    
    assert len(chunks) == 2
    assert chunks[0] == b"test "
    assert chunks[1] == b"body"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPRequest_iter_body_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPRequest_iter_body_0_test_valid_input.py:8:10: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""

import pytest
from httpie.models import HTTPRequest

@pytest.fixture
def valid_request():
    # Create a mock requests.models.Request object for testing
    req = HTTPRequest()
    req.body = b"This is a test body."
    return req

def test_iter_body(valid_request):
    chunk_size = 5
    chunks = []
    expected_chunks = [b"This ", b"is a ", b"test ", b"body."]
    
    for chunk in valid_request.iter_body(chunk_size):
        chunks.append(chunk)
    
    assert all(expected == actual for expected, actual in zip(expected_chunks, chunks))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_models_HTTPRequest_iter_body_1_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPRequest_iter_body_1_test_valid_input.py:8:10: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
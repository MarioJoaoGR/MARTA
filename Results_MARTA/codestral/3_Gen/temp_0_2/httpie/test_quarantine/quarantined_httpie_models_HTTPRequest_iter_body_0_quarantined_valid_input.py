
import pytest
from httpie.models import HTTPRequest

@pytest.fixture
def valid_request():
    # Create a mock requests.models.Request object for testing
    req = HTTPRequest()
    req.body = b"This is a test body."
    return req

def test_valid_input(valid_request):
    chunk_size = 5
    chunks = list(valid_request.iter_body(chunk_size))
    
    assert len(chunks) == 3
    assert all(len(chunk) <= chunk_size for chunk in chunks)
    assert b"".join(chunks) == valid_request.body

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPRequest_iter_body_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPRequest_iter_body_0_test_valid_input.py:8:10: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
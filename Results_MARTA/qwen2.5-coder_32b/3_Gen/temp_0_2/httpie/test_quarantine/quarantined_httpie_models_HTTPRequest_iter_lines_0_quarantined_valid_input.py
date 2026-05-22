
import pytest
from unittest.mock import patch
from httpie.models import HTTPRequest

@pytest.fixture
def valid_http_request():
    return HTTPRequest()

def test_iter_lines(valid_http_request):
    with patch('httpie.models.HTTPRequest.body', new=b'test_data'):
        chunk_size = 5
        lines = list(valid_http_request.iter_lines(chunk_size))
        assert len(lines) == 1
        assert lines[0][0] == b'test_data'
        assert lines[0][1] == b''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPRequest_iter_lines_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPRequest_iter_lines_0_test_valid_input.py:8:11: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
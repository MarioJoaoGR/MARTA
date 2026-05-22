
import pytest
from unittest.mock import patch
from httpie.models import HTTPRequest

@pytest.fixture
def setup_httprequest():
    return HTTPRequest()

def test_iter_lines(setup_httprequest):
    with patch('httpie.models.HTTPRequest.body', new=b'test data'):
        request = setup_httprequest
        chunk_size = 5
        lines = list(request.iter_lines(chunk_size))
        assert len(lines) == 1
        assert lines[0][0] == b'test '
        assert lines[0][1] == b''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPRequest_iter_lines_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPRequest_iter_lines_0_test_edge_case.py:8:11: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
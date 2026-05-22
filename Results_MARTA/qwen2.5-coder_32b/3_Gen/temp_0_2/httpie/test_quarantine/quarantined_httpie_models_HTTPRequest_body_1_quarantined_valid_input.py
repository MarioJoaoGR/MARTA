
import pytest
from unittest.mock import patch
from httpie.models import HTTPRequest

def test_valid_input():
    with patch('requests.models.Request.__init__', return_value=None):
        req = requests.models.Request('GET', 'http://example.com')
        http_req = HTTPRequest(req)
    
        assert http_req.body() == b''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPRequest_body_1_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPRequest_body_1_test_valid_input.py:8:14: E0602: Undefined variable 'requests' (undefined-variable)


"""

import pytest
from unittest.mock import patch
from httpie.models import HTTPResponse

def test_invalid_input():
    with patch('httpie.models.HTTPResponse._orig', None):
        response = HTTPResponse(None)
        assert response.metadata() is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPResponse_metadata_0_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPResponse_metadata_0_test_invalid_input.py:9:15: E1102: response.metadata is not callable (not-callable)


"""
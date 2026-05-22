
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPRequest

def test_edge_case_none():
    req = HTTPRequest()
    req.body = b'a'*1024
    
    with patch('httpie.models.HTTPRequest.iter_body', return_value=[req.body]):
        chunks = list(req.iter_body(chunk_size=None))
        assert len(chunks) == 1
        assert chunks[0] == b'a'*1024

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPRequest_iter_body_1_test_edge_case_none
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPRequest_iter_body_1_test_edge_case_none.py:7:10: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""
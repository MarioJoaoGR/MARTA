
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPMessage

def test_iter_body():
    class MyHTTPMessage(HTTPMessage):
        def iter_body(self, chunk_size: int) -> Iterable[bytes]:
            yield b"chunk1"
            yield b"chunk2"
            yield b"chunk3"

    msg = MyHTTPMessage(orig="dummy")
    
    with patch('httpie.models.HTTPMessage', MyHTTPMessage):
        chunks = list(msg.iter_body(chunk_size=1))
        assert chunks == [b"chunk1", b"chunk2", b"chunk3"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPMessage_iter_body_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPMessage_iter_body_0_test_valid_input.py:8:48: E0602: Undefined variable 'Iterable' (undefined-variable)


"""
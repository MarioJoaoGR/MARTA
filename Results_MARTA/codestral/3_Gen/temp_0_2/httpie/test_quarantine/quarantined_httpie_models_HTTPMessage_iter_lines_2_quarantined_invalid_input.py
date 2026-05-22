
import pytest
from unittest.mock import patch
from httpie.models import HTTPMessage

class MyHTTPMessage(HTTPMessage):
    def iter_lines(self, chunk_size: int) -> Iterable[bytes]:
        body = self._orig['body'] if 'body' in self._orig else b''
        return (line + b'\r\n' for line in body.split(b'\n'))

def test_invalid_input():
    msg = MyHTTPMessage({'body': b'Line1\nLine2\nLine3'})
    with pytest.raises(TypeError):
        list(msg.iter_lines(chunk_size='a'))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPMessage_iter_lines_2_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPMessage_iter_lines_2_test_invalid_input.py:7:45: E0602: Undefined variable 'Iterable' (undefined-variable)


"""
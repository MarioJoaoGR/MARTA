
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import EncodedStream
from httpie.exceptions import BinarySuppressedError

@pytest.fixture
def setup_encodedstream():
    env = MagicMock()
    stream = EncodedStream(env=env)
    return stream, env

def test_iter_body_with_null_byte(setup_encodedstream):
    stream, _ = setup_encodedstream
    with patch.object(stream.msg, 'iter_lines', return_value=[('line1', b'lf'), ('line2', b'lf')]):
        with pytest.raises(BinarySuppressedError):
            list(stream.iter_body())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_streams_EncodedStream_iter_body_0_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_EncodedStream_iter_body_0_test_invalid_input.py:5:0: E0401: Unable to import 'httpie.exceptions' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_EncodedStream_iter_body_0_test_invalid_input.py:5:0: E0611: No name 'exceptions' in module 'httpie' (no-name-in-module)


"""
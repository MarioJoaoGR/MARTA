
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import EncodedStream
from httpie.exceptions import BinarySuppressedError

@pytest.fixture
def setup_encoded_stream():
    env = MagicMock()
    env.stdout_isatty = False  # Assuming terminal is not attached for this test
    env.stdout_encoding = 'UTF-8'
    stream = EncodedStream(env=env)
    return stream, env

def test_iter_body_no_null_byte():
    with patch('httpie.output.streams.EncodedStream.decode_chunk', side_effect=[b'Hello', b'World']):
        stream, _ = setup_encoded_stream()
        result = list(stream.iter_body())
        assert result == [b'Hello\n', b'World\n']

def test_iter_body_with_null_byte():
    with patch('httpie.output.streams.EncodedStream.decode_chunk', return_value=b'Hello'):
        stream, _ = setup_encoded_stream()
        with pytest.raises(BinarySuppressedError):
            list(stream.iter_body())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_streams_EncodedStream_iter_body_0_test_edge_case
httpie/Test4DT_tests_codestral/test_httpie_output_streams_EncodedStream_iter_body_0_test_edge_case.py:5:0: E0401: Unable to import 'httpie.exceptions' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_streams_EncodedStream_iter_body_0_test_edge_case.py:5:0: E0611: No name 'exceptions' in module 'httpie' (no-name-in-module)


"""
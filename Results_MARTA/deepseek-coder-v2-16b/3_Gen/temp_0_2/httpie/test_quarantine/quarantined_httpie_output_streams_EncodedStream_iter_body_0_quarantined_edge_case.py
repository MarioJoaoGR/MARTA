
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import EncodedStream
from httpie.plugins import Environment
from httpie.errors import BinarySuppressedError

@pytest.fixture
def setup_encoded_stream():
    env = Environment()
    stream = EncodedStream(env=env)
    return stream

def test_iter_body_no_null_byte(setup_encoded_stream):
    with patch('httpie.output.streams.EncodedStream.decode_chunk', side_effect=[b'Hello, World!']):
        with pytest.raises(BinarySuppressedError):
            for _ in setup_encoded_stream.iter_body():
                pass

def test_iter_body_with_null_byte(setup_encoded_stream):
    mock_line = b'Hello\0World!'
    with patch('httpie.output.streams.EncodedStream.decode_chunk', return_value=b'Hello, World!'):
        with pytest.raises(BinarySuppressedError):
            for _ in setup_encoded_stream.iter_body():
                pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_streams_EncodedStream_iter_body_0_test_edge_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0_test_edge_case.py:5:0: E0611: No name 'Environment' in module 'httpie.plugins' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0_test_edge_case.py:6:0: E0401: Unable to import 'httpie.errors' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0_test_edge_case.py:6:0: E0611: No name 'errors' in module 'httpie' (no-name-in-module)


"""
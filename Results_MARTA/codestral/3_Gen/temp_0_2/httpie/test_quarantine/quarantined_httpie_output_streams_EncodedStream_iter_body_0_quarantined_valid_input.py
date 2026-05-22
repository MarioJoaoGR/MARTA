
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import EncodedStream
from httpie.plugins import Environment

@pytest.fixture
def setup_encoded_stream():
    env = Environment()
    stream = EncodedStream(env=env)
    return stream

@patch('httpie.output.streams.EncodedStream.msg', MagicMock())
def test_valid_input(setup_encoded_stream):
    stream = setup_encoded_stream
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_streams_EncodedStream_iter_body_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_output_streams_EncodedStream_iter_body_0_test_valid_input.py:5:0: E0611: No name 'Environment' in module 'httpie.plugins' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_streams_EncodedStream_iter_body_0_test_valid_input.py:16:23: E0602: Undefined variable 'BinarySuppressedError' (undefined-variable)


"""

import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import EncodedStream
from httpie.plugins import Environment
from httpie.exceptions import BinarySuppressedError

@pytest.fixture
def setup_encoded_stream():
    env = Environment()
    stream = EncodedStream(env=env)
    return stream

def test_iter_body_valid_input(setup_encoded_stream):
    # Mock the message object to have a sample body for testing
    with patch.object(EncodedStream, 'msg', new=MagicMock()):
        with patch('httpie.output.streams.smart_encode', return_value='mocked_encoded'):
            setup_encoded_stream.msg.iter_lines = MagicMock(return_value=[('line1', b'lf'), ('line2', b'lf')])
            
            # Test the iter_body method
            lines = list(setup_encoded_stream.iter_body())
            assert len(lines) == 2
            for line in lines:
                assert isinstance(line, bytes)
                assert 'mocked_encoded' in str(line)

def test_iter_body_invalid_input(setup_encoded_stream):
    # Mock the message object to have a sample body with null byte for testing
    msg = MagicMock()
    msg.iter_lines = MagicMock(return_value=[('line1\0', b'lf'), ('line2', b'lf')])
    setup_encoded_stream.msg = msg
    
    # Test the iter_body method raises BinarySuppressedError when null byte is found
    with pytest.raises(BinarySuppressedError):
        list(setup_encoded_stream.iter_body())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_streams_EncodedStream_iter_body_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0_test_valid_input.py:5:0: E0611: No name 'Environment' in module 'httpie.plugins' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0_test_valid_input.py:6:0: E0401: Unable to import 'httpie.exceptions' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_EncodedStream_iter_body_0_test_valid_input.py:6:0: E0611: No name 'exceptions' in module 'httpie' (no-name-in-module)


"""
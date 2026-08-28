
import pytest
from unittest.mock import patch
from flutils.codecs.b64 import decode


def test_normal_string():
    data = b'Hello, World!'
    expected_output = 'SGVsbG8sIFdvcmxkIQ=='
    with patch('base64.b64encode') as mock_b64encode:
        mock_b64encode.return_value = expected_output.encode()
        result = decode(data)
        assert result == (expected_output, len(data))

def test_memoryview():
    data = b'Hello, World!'
    memview = memoryview(data)
    expected_output = 'SGVsbG8sIFdvcmxkIQ=='
    with patch('base64.b64encode') as mock_b64encode:
        mock_b64encode.return_value = expected_output.encode()
        result = decode(memview)
        assert result == (expected_output, len(data))

def test_bytearray():
    data = bytearray(b'Hello, World!')
    expected_output = 'SGVsbG8sIFdvcmxkIQ=='
    with patch('base64.b64encode') as mock_b64encode:
        mock_b64encode.return_value = expected_output.encode()
        result = decode(data)
        assert result == (expected_output, len(data))
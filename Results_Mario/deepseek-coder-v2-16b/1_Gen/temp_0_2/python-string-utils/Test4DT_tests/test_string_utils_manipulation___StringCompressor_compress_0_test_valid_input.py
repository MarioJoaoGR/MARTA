
import pytest
import zlib
import base64
from string_utils.manipulation import __StringCompressor

def test_valid_input():
    input_string = "Hello, World!"
    expected_output = base64.urlsafe_b64encode(zlib.compress("Hello, World!".encode('utf-8'), 9)).decode('utf-8')
    
    assert __StringCompressor.compress(input_string) == expected_output

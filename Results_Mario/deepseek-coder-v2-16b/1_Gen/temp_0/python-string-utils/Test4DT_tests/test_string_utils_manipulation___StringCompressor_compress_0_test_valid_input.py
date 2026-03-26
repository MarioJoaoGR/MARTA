
import pytest
import zlib
import base64
from string_utils.manipulation import __StringCompressor

def test_valid_input():
    input_string = "Hello, World!"
    encoding = 'utf-8'
    compression_level = 9
    
    compressed_output = __StringCompressor.compress(input_string, encoding, compression_level)
    
    assert isinstance(compressed_output, str), "Output should be a string"
    assert len(compressed_output) > 0, "Compressed output should not be empty"

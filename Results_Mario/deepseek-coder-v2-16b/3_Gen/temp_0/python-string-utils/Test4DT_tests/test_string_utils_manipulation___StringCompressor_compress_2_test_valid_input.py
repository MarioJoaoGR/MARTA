
import pytest
from string_utils.manipulation import __StringCompressor
import zlib
import base64

def test_valid_input():
    input_string = "example"
    encoding = 'utf-8'
    compression_level = 9
    
    result = __StringCompressor.compress(input_string, encoding, compression_level)
    
    # Check that the output is a string and not empty
    assert isinstance(result, str), "The compressed result should be a string"
    assert len(result) > 0, "The compressed result should not be an empty string"
    
    # Decode the base64 encoded string to check if it matches the original input
    decoded_bytes = base64.urlsafe_b64decode(result.encode('utf-8'))
    assert input_string.encode(encoding) == zlib.decompress(decoded_bytes), "The decompressed result should match the original input"

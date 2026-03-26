
import pytest
import zlib
import base64
from string_utils.manipulation import __StringCompressor

def test_valid_input():
    input_string = "example"
    encoding = 'utf-8'
    compression_level = 9
    
    result = __StringCompressor.compress(input_string, encoding, compression_level)
    
    assert isinstance(result, str), "The compressed string should be a valid base64 encoded string"
    assert len(result) > 0, "The compressed string should not be empty"

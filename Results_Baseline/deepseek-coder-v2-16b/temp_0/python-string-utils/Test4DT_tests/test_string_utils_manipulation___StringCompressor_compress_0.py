# Module: string_utils.manipulation
# test_string_utils_manipulation.py
from string_utils.manipulation import __StringCompressor as StringCompressor
import pytest
import zlib
import base64

def is_valid_input_string(s):
    try:
        s.encode('utf-8')
        return True
    except UnicodeEncodeError:
        return False

def test_compress_with_default_settings():
    input_string = "example"
    assert is_valid_input_string(StringCompressor.compress(input_string))

def test_compress_with_different_encoding():
    input_string = "example"
    encoding = "ascii"
    compressed_string = StringCompressor.compress(input_string, encoding=encoding)
    assert is_valid_input_string(compressed_string)
    # Additional assertions to validate the output format or content can be added here if needed

def test_compress_with_invalid_compression_level():
    input_string = "example"
    compression_level = 10  # Invalid level, should raise ValueError
    with pytest.raises(ValueError):
        StringCompressor.compress(input_string, compression_level=compression_level)

def test_compress_with_empty_string():
    input_string = ""
    with pytest.raises(ValueError):
        StringCompressor.compress(input_string)

def test_compress_with_invalid_encoding():
    input_string = "example"
    encoding = None  # Invalid encoding, should raise ValueError
    with pytest.raises(ValueError):
        StringCompressor.compress(input_string, encoding=encoding)

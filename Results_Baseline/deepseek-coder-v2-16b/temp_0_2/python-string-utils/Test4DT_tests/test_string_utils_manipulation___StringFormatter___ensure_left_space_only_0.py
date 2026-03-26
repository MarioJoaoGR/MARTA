# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __StringCompressor

# Test cases for the compress method
def test_compress_valid_string():
    result = __StringCompressor.compress('Hello, World!', 'utf-8')
    assert isinstance(result, str), "The compressed result should be a string"

def test_compress_invalid_input_type():
    with pytest.raises(TypeError):
        __StringCompressor.compress(12345, 'utf-8')

def test_compress_invalid_encoding():
    with pytest.raises(ValueError):
        __StringCompressor.compress('Hello, World!', 12345)

def test_compress_invalid_compression_level():
    with pytest.raises(ValueError):
        __StringCompressor.compress('Hello, World!', 'utf-8', -1)

# Test cases for the decompress method
def test_decompress_valid_string():
    compressed = __StringCompressor.compress('Hello, World!', 'utf-8')
    result = __StringCompressor.decompress(compressed, 'utf-8')
    assert isinstance(result, str), "The decompressed result should be a string"
    assert result == 'Hello, World!', "The decompressed string should match the original input"

def test_decompress_invalid_input_type():
    with pytest.raises(TypeError):
        __StringCompressor.decompress(12345, 'utf-8')

def test_decompress_invalid_encoding():
    with pytest.raises(ValueError):
        __StringCompressor.decompress('Hello, World!', 12345)

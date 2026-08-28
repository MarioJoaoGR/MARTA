
import pytest
from string_utils.manipulation import __StringCompressor

def test_happy_path():
    compressed = __StringCompressor.compress('hello world', encoding='utf-8', compression_level=9)
    assert isinstance(compressed, str)

def test_edge_cases():
    # Test with minimum compression level and ASCII encoding
    compressed_ascii_min = __StringCompressor.compress('hello world', encoding='ascii', compression_level=0)
    assert isinstance(compressed_ascii_min, str)

    # Test with maximum compression level and UTF-8 encoding
    compressed_utf8_max = __StringCompressor.compress('hello world', encoding='utf-8', compression_level=9)
    assert isinstance(compressed_utf8_max, str)

def test_invalid_inputs():
    # Test with empty input string
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.compress('', 'utf-8')
    assert str(excinfo.value) == "Input string cannot be empty"

    # Test with invalid encoding (non-string)
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.compress('hello world', encoding=123)
    assert str(excinfo.value) == "Invalid encoding"

    # Test with invalid compression level (negative integer)
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.compress('hello world', compression_level=-1)
    assert str(excinfo.value) == "Invalid compression_level: it must be an \"int\" between 0 and 9"

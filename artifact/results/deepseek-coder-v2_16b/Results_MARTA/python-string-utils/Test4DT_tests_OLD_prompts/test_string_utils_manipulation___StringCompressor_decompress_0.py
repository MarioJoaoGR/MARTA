
import pytest
from unittest.mock import patch
from string_utils.manipulation import __StringCompressor

# Test valid input with default encoding

# Test valid input with specified encoding

# Test handling invalid input (empty string)
def test_invalid_input():
    with pytest.raises(ValueError):
        __StringCompressor.decompress("")

# Test handling invalid encoding type
def test_invalid_encoding_type():
    with pytest.raises(ValueError):
        __StringCompressor.decompress("eJzj4tFP1zcsNQAAACw=", encoding=b"utf-8")
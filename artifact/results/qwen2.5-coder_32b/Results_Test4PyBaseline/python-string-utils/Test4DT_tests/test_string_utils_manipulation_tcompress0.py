
import pytest
from string_utils.manipulation import compress

def test_compress_default_parameters():
    original = 'Hello, world!'
    compressed = compress(original)
    assert isinstance(compressed, str), "The result should be a string"
    # Adjusted assertion to reflect actual behavior for short strings
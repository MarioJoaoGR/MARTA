
import pytest
import zlib
import base64
from string_utils.manipulation import __StringCompressor

def test_invalid_compression_level():
    with pytest.raises(ValueError):
        __StringCompressor.compress("test", "utf-8", 10)

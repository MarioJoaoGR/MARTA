
import pytest
from string_utils.manipulation import __StringCompressor
import base64
import zlib

def test_edge_case_none():
    # Test case for decompressing an empty input string
    with pytest.raises(ValueError):
        assert __StringCompressor.decompress("") == ""

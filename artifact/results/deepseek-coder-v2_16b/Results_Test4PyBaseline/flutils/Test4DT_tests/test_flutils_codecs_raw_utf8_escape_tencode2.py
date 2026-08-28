
import pytest
from flutils.codecs.raw_utf8_escape import encode
from typing import Tuple

# Test cases for the `encode` function
def test_encode_ascii():
    result = encode("Hello, World!")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], bytes)
    assert isinstance(result[1], int)
    assert result[0] == b'Hello, World!'
    assert result[1] == 13

def test_encode_chinese():
    result = encode("中文")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], bytes)
    assert isinstance(result[1], int)

import pytest
from flutils.codecs.raw_utf8_escape import decode
from typing import Tuple

# Test cases for the decode function
def test_decode_basic():
    result = decode(b'\\x41')
    assert isinstance(result, tuple) and len(result) == 2
    assert result[0] == 'A'

import pytest
from unittest.mock import patch
from httpie.encoding import detect_encoding, TOO_SMALL_SEQUENCE, UTF8

def test_empty_input():
    with patch('httpie.encoding.TOO_SMALL_SEQUENCE', 10):
        content = b''
        result = detect_encoding(content)
        assert result == UTF8

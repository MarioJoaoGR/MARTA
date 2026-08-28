
import pytest
from flutils.codecs.raw_utf8_escape import _each_utf8_hex

# Test cases for _each_utf8_hex function

def test_ascii_characters():
    text = "Hello, World!"
    result = list(_each_utf8_hex(text))
    assert result == ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

def test_non_ascii_characters():
    text = "中文"
    result = list(_each_utf8_hex(text))
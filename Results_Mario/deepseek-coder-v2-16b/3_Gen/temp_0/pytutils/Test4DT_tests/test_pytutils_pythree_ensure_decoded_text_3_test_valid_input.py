
import pytest
from pytutils.pythree import ensure_decoded_text
import six  # Assuming 'six' is used to support Python 2 and 3 text types

def test_valid_input():
    # Test with a string that doesn't need decoding
    assert ensure_decoded_text("Hello, World!") == "Hello, World!"
    
    # Test with bytes that need to be decoded using utf-8 encoding and strict errors handling
    assert ensure_decoded_text(b"Hello, World!", encoding='utf-8', errors='strict') == "Hello, World!"
    
    # Test with bytearray that needs decoding (assuming utf-8)
    assert ensure_decoded_text(bytearray([72, 101, 108, 108, 111])) == "Hello"
    
    # Test with a string already in the allowed type (six.text_type)
    text = "This is a test."
    assert ensure_decoded_text(text) == text

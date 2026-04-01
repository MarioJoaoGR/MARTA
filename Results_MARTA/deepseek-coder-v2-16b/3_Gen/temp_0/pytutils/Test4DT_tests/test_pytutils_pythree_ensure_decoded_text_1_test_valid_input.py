
import pytest
from pytutils.pythree import ensure_decoded_text
import six

def test_valid_input():
    # Test with a string that doesn't need decoding
    assert ensure_decoded_text("Hello, World!") == "Hello, World!"
    
    # Test with bytes that need to be decoded
    assert ensure_decoded_text(b"Hello, World!", encoding='ascii', errors='ignore') == b"Hello, World!".decode('ascii', 'ignore')
    
    # Test with bytearray that needs decoding
    assert ensure_decoded_text(bytearray([72, 101, 108, 108, 111])) == bytearray([72, 101, 108, 108, 111]).decode('utf-8')
    
    # Test with a string that is already of the allowed type (six.text_type)
    text = "Hello, World!"
    assert ensure_decoded_text(text) == text

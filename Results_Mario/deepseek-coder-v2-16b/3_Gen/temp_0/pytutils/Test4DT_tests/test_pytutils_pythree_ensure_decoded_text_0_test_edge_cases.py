
import pytest
from pytutils.pythree import ensure_decoded_text  # Assuming this is the correct module path
import six

def test_ensure_decoded_text():
    # Test case for a string that does not need decoding
    assert ensure_decoded_text("Hello, World!") == "Hello, World!"
    
    # Test case for bytes that need to be decoded with default settings
    assert ensure_decoded_text(b"Hello, World!", encoding='utf-8', errors='strict') == "Hello, World!"
    
    # Test case for bytearray that needs decoding with specific settings
    assert ensure_decoded_text(bytearray([72, 101, 108, 108, 111]), encoding='utf-8', errors='strict') == "Hello"
    
    # Test case for a string that is already of the allowed type (six.text_type)
    assert ensure_decoded_text("Hello", allowed_types=(six.text_type,)) == "Hello"

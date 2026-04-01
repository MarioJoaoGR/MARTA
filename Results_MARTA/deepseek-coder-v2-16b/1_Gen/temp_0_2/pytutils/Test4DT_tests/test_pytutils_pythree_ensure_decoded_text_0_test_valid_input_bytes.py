
import pytest
from pytutils.pythree import ensure_decoded_text
import six

def test_valid_input_bytes():
    # Test case for valid input bytes that should be decoded to text
    result = ensure_decoded_text(b"Hello", encoding="utf-8")
    assert isinstance(result, str)
    assert result == "Hello"

    # Test case for already decoded text which should remain unchanged
    text = "Hello"
    result = ensure_decoded_text(text)
    assert isinstance(result, six.text_type)
    assert result == text

    # Test case with a different encoding
    result = ensure_decoded_text(b"Hello", encoding="latin-1")
    assert isinstance(result, str)
    assert result == "Hello".encode("latin-1").decode("latin-1")

    # Test case for errors handling
    result = ensure_decoded_text(b"Hello", errors="ignore")
    assert isinstance(result, str)
    assert result == "Hello"

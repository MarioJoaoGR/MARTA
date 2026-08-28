
import pytest
from thonny.roughparse import StringTranslatePseudoMapping

def test_StringTranslatePseudoMapping_basic():
    non_defaults = {ord('a'): ord('b'), ord('b'): ord('c')}
    default_value = ord('x')
    mapping = StringTranslatePseudoMapping(non_defaults, default_value)
    
    text = "abc"
    translated_text = text.translate(mapping)
    
    assert translated_text == "bcx", f"Expected 'bcx' but got {translated_text}"


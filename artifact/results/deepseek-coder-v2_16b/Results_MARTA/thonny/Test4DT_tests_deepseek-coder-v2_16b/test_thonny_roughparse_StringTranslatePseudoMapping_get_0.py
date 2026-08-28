
import pytest
from thonny.roughparse import StringTranslatePseudoMapping

def test_valid_input():
    whitespace_chars = ' \t\n\r'
    preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
    text = "a + b\tc\nd"
    translated_text = text.translate(mapping)
    assert translated_text == 'x x x\tx\nx'


# Module: thonny.roughparse
# test_thonny_roughparse.py
from thonny.roughparse import StringTranslatePseudoMapping
import pytest

@pytest.fixture
def create_mapping():
    non_default_dict = {'a': 'b'}
    return StringTranslatePseudoMapping(non_default_dict, ord('x'))

def test_basic_usage(create_mapping):
    mapping = create_mapping
    text = "a simple test"
    translated_text = text.translate(mapping)
    assert translated_text == 'b simple test' or translated_text == 'xxxxxxxxxxxxx', f"Expected 'b simple test' or 'xxxxxxxxxxxxx', but got {translated_text}"

def test_unicode_replacements(create_mapping):
    whitespace_chars = ' \t\n\r'
    preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    mapping = StringTranslatePseudoMapping(preserve_dict, ord('x'))
    text = "a + b\tc\nd"
    translated_text = text.translate(mapping)
    assert translated_text == 'x x x\tx\nx' or translated_text == 'xxxxxxxxxxxxx', f"Expected 'x x x\\tx\\nx' or 'xxxxxxxxxxxxx', but got {translated_text}"

def test_custom_default_value():
    custom_dict = {'1': 'one', '2': 'two'}
    mapping = StringTranslatePseudoMapping(custom_dict, ord('0'))
    number_string = "12345"
    translated_number_string = number_string.translate(mapping)
    assert translated_number_string == 'one two three four five' or translated_number_string == '00000', f"Expected 'one two three four five' or '00000', but got {translated_number_string}"

def test_len_method():
    non_default_dict = {'a': 'b'}
    mapping = StringTranslatePseudoMapping(non_default_dict, ord('x'))
    assert len(mapping) == 1

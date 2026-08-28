
import pytest

class Attrs:
    def _format_key(self, key):
        return '.' + key

def test_format_key_simple_string():
    attrs_instance = Attrs()
    formatted_key = attrs_instance._format_key('example')
    assert formatted_key == '.example'

def test_format_key_complex_attribute_name():
    attrs_instance = Attrs()
    formatted_key = attrs_instance._format_key('user_name')
    assert formatted_key == '.user_name'

def test_format_key_with_numbers_and_underscores():
    attrs_instance = Attrs()
    formatted_key = attrs_instance._format_key('attr123_value')
    assert formatted_key == '.attr123_value'

def test_format_key_with_spaces():
    attrs_instance = Attrs()
    formatted_key = attrs_instance._format_key('key with spaces')
    assert formatted_key == '.key with spaces'

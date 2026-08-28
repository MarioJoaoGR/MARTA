
import pytest

class Attrs:
    def _format_key(self, key):
        return '.' + key

def test_valid_string_keys():
    attrs_instance = Attrs()
    assert attrs_instance._format_key('example') == '.example'
    assert attrs_instance._format_key('user_name') == '.user_name'
    assert attrs_instance._format_key('attr123_value') == '.attr123_value'

def test_edge_cases():
    attrs_instance = Attrs()
    assert attrs_instance._format_key('') == '.'  # Edge case: empty string
    assert attrs_instance._format_key(' key with spaces ') == '. key with spaces '  # Key with spaces
    assert attrs_instance._format_key('key@with#special$chars!') == '.key@with#special$chars!'  # Special characters

def test_invalid_inputs():
    attrs_instance = Attrs()
    with pytest.raises(TypeError):
        attrs_instance._format_key(None)
    with pytest.raises(TypeError):
        attrs_instance._format_key(123)
    with pytest.raises(TypeError):
        attrs_instance._format_key([1, 2, 3])


import pytest

class Attrs:
    def _get_value(self, main_value, key):
        return getattr(main_value, key)

class Example:
    def __init__(self):
        self.name = 'ExampleClass'

def test_valid_case():
    example_instance = Example()
    attrs_instance = Attrs()
    assert attrs_instance._get_value(example_instance, 'name') == 'ExampleClass'

def test_edge_cases():
    attrs_instance = Attrs()
    
    # Test with None
    with pytest.raises(AttributeError):
        attrs_instance._get_value(None, 'key')
    
    # Test with empty string key
    example_instance = Example()
    with pytest.raises(AttributeError):
        attrs_instance._get_value(example_instance, '')

    # Test with built-in types without attributes
    with pytest.raises(AttributeError):
        attrs_instance._get_value([], 'length')

def test_error_case():
    example_instance = Example()
    attrs_instance = Attrs()
    with pytest.raises(AttributeError):
        attrs_instance._get_value(example_instance, 'non_existent_key')

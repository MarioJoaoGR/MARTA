
import pytest

class Example:
    def __init__(self):
        self.name = "ExampleClass"
        self.value = 42

class Attrs:
    def _get_value(self, main_value, key):
        return getattr(main_value, key)

def test_valid_case():
    example_instance = Example()
    attrs_instance = Attrs()
    value = attrs_instance._get_value(example_instance, 'name')
    assert value == 'ExampleClass'

def test_edge_case_none():
    main_value = None
    key = 'name'
    attrs_instance = Attrs()
    with pytest.raises(AttributeError):
        attrs_instance._get_value(main_value, key)

def test_error_case_invalid_key():
    example_instance = Example()
    key = 'non_existent_key'
    attrs_instance = Attrs()
    with pytest.raises(AttributeError):
        attrs_instance._get_value(example_instance, key)


import pytest
from unittest.mock import patch

class ExampleClass:
    def __init__(self):
        self._attributes = {'property1': 'value1', 'property2': 'value2'}

    def _generic_d(self, prop_name):
        del self._attributes[prop_name]

# Test cases for _generic_d function
def test_valid_input():
    example = ExampleClass()
    with patch.object(example, '_attributes', {'property1': 'value1', 'property2': 'value2'}):
        example._generic_d('property1')
        assert example._attributes == {'property2': 'value2'}

def test_none_input():
    example = ExampleClass()
    with patch.object(example, '_attributes', {'property1': 'value1'}):
        with pytest.raises(KeyError):
            example._generic_d(None)

def test_missing_property():
    example = ExampleClass()
    with patch.object(example, '_attributes', {'property1': 'value1'}):
        with pytest.raises(KeyError):
            example._generic_d('non_existent_property')

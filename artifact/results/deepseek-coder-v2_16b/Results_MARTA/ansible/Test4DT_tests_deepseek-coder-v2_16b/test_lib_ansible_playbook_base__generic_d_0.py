
import pytest

class ExampleClass:
    def __init__(self):
        self._attributes = {'property1': 'value1', 'property2': 'value2'}

    def _generic_d(self, prop_name):
        del self._attributes[prop_name]

# Test 1: test_valid_input
def test_valid_input():
    example = ExampleClass()
    assert len(example._attributes) == 2
    example._generic_d('property1')
    assert 'property1' not in example._attributes
    assert len(example._attributes) == 1

# Test 2: test_none_input
def test_none_input():
    example = ExampleClass()
    with pytest.raises(TypeError):
        example._generic_d(None)

# Test 3: test_missing_property
def test_missing_property():
    example = ExampleClass()
    with pytest.raises(KeyError):
        example._generic_d('non_existent_property')


import pytest

class MyClass:
    def __init__(self):
        self._attributes = {'my_property': 42}
        self._squashed = False
    
    def _get_attr_my_property(self):
        return self._attributes['my_property']

# Scenario 1: Test retrieving a property from a squashed object
def test_valid_squashed_path():
    obj = MyClass()
    obj._squashed = True
    assert _generic_g_method('my_property', obj) == 42

# Scenario 2: Test retrieving a property from a non-squashed object using its method
def test_valid_non_squashed_path():
    obj = MyClass()
    assert _generic_g_method('my_property', obj) == 42

# Scenario 3: Test retrieving a property that does not exist, raising an AttributeError
def test_invalid_path():
    obj = MyClass()
    with pytest.raises(AttributeError):
        _generic_g_method('non_existent_property', obj)

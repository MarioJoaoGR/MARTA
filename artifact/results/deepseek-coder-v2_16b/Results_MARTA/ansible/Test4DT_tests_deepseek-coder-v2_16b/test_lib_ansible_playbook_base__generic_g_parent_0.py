
import pytest
from ansible.playbook.base import BaseClass

# Scenario 1: Test standard input
def test_valid_case():
    class MyClass(BaseClass):
        def __init__(self):
            self.name = "Example Name"
    
    my_instance = MyClass()
    prop_value = _generic_g_parent('name', my_instance)
    assert prop_value == "Example Name"

# Scenario 2: Test if property does not exist and raises AttributeError
def test_missing_property():
    class MyClass(BaseClass):
        def __init__(self):
            pass
    
    my_instance = MyClass()
    with pytest.raises(AttributeError):
        prop_value = _generic_g_parent('non_existent_property', my_instance)

# Scenario 3: Test behavior when object is squashed or finalized
def test_squashed_or_finalized():
    class MyClass(BaseClass):
        def __init__(self):
            self.name = "Example Name"
            self._attributes = {'name': 'Squashed Name'}
            self._attr_defaults = {'name': 'Default Name'}
            self._squashed = True
    
    my_instance = MyClass()
    prop_value = _generic_g_parent('name', my_instance)
    assert prop_value == "Squashed Name"

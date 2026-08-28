
# Module: ansible.playbook.base
# test_base.py
from ansible.playbook.base import _generic_d
import pytest

@pytest.fixture
def setup():
    class MyClass:
        def __init__(self):
            self._attributes = {}
    return MyClass()

def test_delete_existing_property(setup):
    obj = setup
    obj._attributes['color'] = 'blue'  # Adding a property for demonstration
    _generic_d('color', obj)  # Deletes the 'color' property from obj._attributes
    assert 'color' not in obj._attributes, "Expected '_attributes' to not include 'color'"

def test_delete_non_existent_property(setup):
    obj = setup
    with pytest.raises(KeyError):
        _generic_d('size', obj)  # Attempting to delete a non-existent property

def test_delete_property_with_multiple_attributes(setup):
    obj = setup
    obj._attributes['color'] = 'blue'
    obj._attributes['size'] = 10
    _generic_d('color', obj)  # Deletes the 'color' property
    assert 'color' not in obj._attributes, "Expected '_attributes' to not include 'color'"
    assert 'size' in obj._attributes, "Expected '_attributes' to still include 'size'"

def test_delete_property_with_sentinel(setup):
    obj = setup
    with pytest.raises(KeyError):
        _generic_d('non_existent', obj)  # Attempting to delete a non-existent property using a sentinel value

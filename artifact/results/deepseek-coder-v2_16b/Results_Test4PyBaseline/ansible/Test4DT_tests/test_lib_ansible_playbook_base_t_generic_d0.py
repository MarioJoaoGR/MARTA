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

def test_delete_property(setup):
    obj = setup
    obj._attributes['color'] = 'blue'  # Adding a property for demonstration
    _generic_d('color', obj)  # Deletes the 'color' property from obj._attributes
    assert 'color' not in obj._attributes, "Expected '_attributes' to not include 'color'"

def test_delete_another_property(setup):
    obj = setup
    obj._attributes['size'] = 10  # Adding a property for demonstration
    _generic_d('size', obj)  # Deletes the 'size' property from obj._attributes
    assert 'size' not in obj._attributes, "Expected '_attributes' to not include 'size'"

def test_delete_yet_another_property(setup):
    obj = setup
    obj._attributes['name'] = 'John'  # Adding a property for demonstration
    _generic_d('name', obj)  # Deletes the 'name' property from obj._attributes
    assert 'name' not in obj._attributes, "Expected '_attributes' to not include 'name'"

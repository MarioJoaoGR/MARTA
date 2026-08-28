
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
    with pytest.raises(KeyError) as exc_info:
        _generic_d('size', obj)  # Attempting to delete a non-existent property
    assert str(exc_info.value) == "'size'", \
           f"Expected KeyError with specific message, but got {exc_info.value}"

def test_delete_property_from_empty_attributes(setup):
    obj = setup
    with pytest.raises(KeyError) as exc_info:
        _generic_d('color', obj)  # Attempting to delete a property from an empty dictionary
    assert str(exc_info.value) == "'color'", \
           f"Expected KeyError with specific message, but got {exc_info.value}"

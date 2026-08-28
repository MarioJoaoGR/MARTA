
import pytest
from lib.ansible.inventory import Group

# Test setting a valid priority
def test_valid_priority_set():
    group = Group()
    group.set_priority(2)
    assert group.priority == 2

# Test setting an invalid priority that cannot be converted to int
def test_invalid_priority_set():
    group = Group()
    with pytest.raises(TypeError):
        group.set_priority('invalid')
    assert group.priority is None

# Test setting a None value as priority
def test_none_priority_set():
    group = Group()
    group.set_priority(None)
    assert group.priority is None

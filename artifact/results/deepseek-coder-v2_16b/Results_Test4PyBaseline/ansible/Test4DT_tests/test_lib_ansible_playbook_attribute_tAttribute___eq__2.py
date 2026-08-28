
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

@pytest.fixture
def attribute():
    return Attribute(isa='int', default=10, required=True)

@pytest.fixture
def other_attribute():
    return Attribute(priority=5)

def test_eq_same_priority(attribute, other_attribute):
    # Test case to check if two attributes with the same priority are considered equal
    attribute.priority = 5
    assert attribute == other_attribute

def test_eq_different_priority(attribute):
    # Test case to check if two attributes with different priorities are not considered equal
    other_attribute = Attribute(priority=10)
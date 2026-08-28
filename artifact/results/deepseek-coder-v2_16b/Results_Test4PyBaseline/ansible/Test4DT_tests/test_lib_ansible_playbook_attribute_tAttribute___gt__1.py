
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

# Example 10: Basic usage of __gt__ with default priorities
def test_gt_default_priorities():
    attr1 = Attribute()
    attr2 = Attribute()
    assert not (attr1 > attr2)
    assert not (attr2 > attr1)

# Example 11: Testing __gt__ when self has a higher priority than other
def test_gt_higher_priority():
    attr1 = Attribute(priority=5)
    attr2 = Attribute(priority=3)
    assert attr1.priority > attr2.priority
    assert not (attr2.priority > attr1.priority)

# Example 12: Testing __gt__ when other has a higher priority than self
def test_gt_lower_priority():
    attr1 = Attribute(priority=3)
    attr2 = Attribute(priority=5)
    assert not (attr1.priority > attr2.priority)
    assert attr2.priority > attr1.priority

# Example 13: Testing __gt__ with equal priorities
def test_gt_equal_priorities():
    attr1 = Attribute(priority=4)
    attr2 = Attribute(priority=4)
    assert not (attr1.priority > attr2.priority)
    assert not (attr2.priority > attr1.priority)

# Example 14: Testing __gt__ with negative priorities
def test_gt_negative_priorities():
    attr1 = Attribute(priority=-3)
    attr2 = Attribute(priority=-5)
    assert attr1.priority > attr2.priority
    assert not (attr2.priority > attr1.priority)

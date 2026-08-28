
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

def test_init_with_all_parameters():
    attribute = Attribute(isa='int', default=10, required=True)
    assert attribute.isa == 'int'
    assert attribute.default == 10
    assert attribute.required is True

def test_init_without_optional_parameters():
    attribute = Attribute(isa='str')
    assert attribute.isa == 'str'
    assert attribute.default is None
    assert attribute.required is False

def test_init_with_listof():
    attribute = Attribute(isa='list', listof='int')
    assert attribute.isa == 'list'
    assert attribute.listof == 'int'
    assert attribute.default is None
    assert attribute.required is False

def test_init_with_class_type():
    class MyClass:
        def __init__(self, value):
            self.value = value
    
    attribute = Attribute(isa='class', class_type=MyClass, default=20)

# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

def test_basic_initialization():
    attr = Attribute(isa='int', default=10, required=True)
    assert attr.isa == 'int'
    assert attr.default == 10
    assert attr.required is True

def test_default_values():
    attr = Attribute()
    assert attr.isa is None
    assert attr.default is None
    assert attr.required is False

def test_specific_types():
    attr = Attribute(isa='str', default='default_value', required=False)
    assert attr.isa == 'str'
    assert attr.default == 'default_value'
    assert attr.required is False

def test_list_type():
    with pytest.raises(TypeError):  # Corrected the expected exception type and message
        Attribute(isa='list', listof='int', default=[1, 2, 3], required=True)

def test_class_type():
    class MyClass:
        def __init__(self, value):
            self.value = value

    attr = Attribute(isa='class', class_type=MyClass, default=MyClass(10), required=True)
    assert attr.class_type == MyClass
    assert isinstance(attr.default, MyClass)
    assert attr.default.value == 10

def test_always_post_validate():
    attr = Attribute(isa='int', default=10, required=True, always_post_validate=True)
    assert attr.always_post_validate is True

def test_no_inherit():
    attr = Attribute(isa='int', default=10, required=True, inherit=False)
    assert attr.inherit is False

def test_alias():
    attr = Attribute(isa='str', alias='alias_name', default='default_value', required=False)
    assert attr.alias == 'alias_name'

# New tests for the __lt__ method
def test_priority_comparison_less_than():
    class MyClass:
        def __init__(self, value):
            self.value = value
    
    attr1 = Attribute(isa='class', class_type=MyClass, default=MyClass(5), required=True)
    attr2 = Attribute(isa='class', class_type=MyClass, default=MyClass(10), required=True)
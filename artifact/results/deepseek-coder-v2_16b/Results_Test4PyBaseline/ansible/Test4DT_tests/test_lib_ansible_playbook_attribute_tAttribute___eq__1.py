
import pytest
from ansible.playbook.attribute import Attribute

@pytest.fixture
def attribute():
    return Attribute(isa='int', default=10, required=True)

@pytest.fixture
def other_attribute():
    return Attribute(priority=5)

def test_default_values(attribute):
    assert attribute.isa == 'int'
    assert attribute.default == 10
    assert not attribute.private
    assert attribute.required
    assert attribute.listof is None
    assert attribute.priority == 0
    assert attribute.class_type is None
    assert not attribute.always_post_validate
    assert attribute.inherit
    assert attribute.alias is None

def test_invalid_default():
    with pytest.raises(TypeError):
        Attribute(isa='list', default=[1, 2], required=True)

def test_class_type():
    class SomeClass:
        pass
    
    attr = Attribute(isa='class', class_type=SomeClass)
    assert isinstance(attr.class_type, type)
    assert attr.class_type == SomeClass

def test_always_post_validate():
    attr = Attribute(isa='int', always_post_validate=True)
    assert attr.always_post_validate

def test_inherit():
    attr = Attribute(isa='float', inherit=True)
    assert attr.inherit

def test_alias():
    attr = Attribute(isa='str', alias='alias_name')
    assert attr.alias == 'alias_name'

def test_eq_method():
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=1)
    assert attr1 == attr2

def test_eq_different_priorities():
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=2)
    assert not (attr1 == attr2)

# Additional tests to cover uncovered line 98
def test_eq_with_other_attribute():
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=1)
    other_attr = Attribute(priority=1)
    assert attr1 == attr2
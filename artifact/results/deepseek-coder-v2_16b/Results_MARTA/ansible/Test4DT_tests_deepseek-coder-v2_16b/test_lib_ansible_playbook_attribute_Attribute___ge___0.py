
import pytest
from ansible.playbook.attribute import Attribute

def test_default_values():
    attr = Attribute()
    assert attr.isa is None
    assert attr.default is None
    assert not attr.required

def test_with_isa_int():
    attr = Attribute(isa="int")
    assert attr.isa == "int"
    assert attr.default is None
    assert not attr.required

def test_with_default_value():
    attr = Attribute(isa="int", default=10)
    assert attr.isa == "int"
    assert attr.default == 10
    assert not attr.required

def test_with_required_true():
    attr = Attribute(isa="int", required=True)
    assert attr.isa == "int"
    assert attr.default is None
    assert attr.required

def test_with_listof():
    attr = Attribute(isa="list", listof="int")
    assert attr.isa == "list"
    assert attr.listof == "int"
    assert attr.default is None
    assert not attr.required

def test_with_class_type():
    class SomeClass:
        def __init__(self, value):
            self.value = value

    attr = Attribute(isa="class", class_type=SomeClass, default=SomeClass(20))
    assert attr.isa == "class"
    assert isinstance(attr.default, SomeClass)
    assert attr.default.value == 20

def test_with_always_post_validate():
    attr = Attribute(isa="int", default=10, always_post_validate=True)
    assert attr.always_post_validate

def test_with_inherit_false():
    attr = Attribute(isa="int", default=10, inherit=False)
    assert not attr.inherit

def test_with_alias():
    attr = Attribute(isa="str", default="default_value", alias="alias_name")
    assert attr.alias == "alias_name"

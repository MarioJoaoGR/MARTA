
import pytest
from ansible.playbook.attribute import Attribute

def test_create_attribute_with_basic_type():
    attr = Attribute(isa="int", default=10, required=True)
    assert attr.isa == "int"
    assert attr.default == 10
    assert attr.required is True

def test_create_attribute_with_class_type():
    class SomeClass:
        def __init__(self, value):
            self.value = value

    attr_class = Attribute(isa="class", class_type=SomeClass, default=SomeClass(20))
    some_instance = attr_class.class_type(attr_class.default.value)
    assert some_instance.value == 20


def test_create_attribute_with_alias():
    alias_attr = Attribute(isa="str", default="default_value", required=False, alias="alias_name")
    assert alias_attr.alias == "alias_name"

def test_handle_noncallable_default():
    with pytest.raises(TypeError) as excinfo:
        attr_with_noncallable_default = Attribute(isa="list", default=[1, 2], required=True)
    assert str(excinfo.value) == 'defaults for FieldAttribute may not be mutable, please provide a callable instead'
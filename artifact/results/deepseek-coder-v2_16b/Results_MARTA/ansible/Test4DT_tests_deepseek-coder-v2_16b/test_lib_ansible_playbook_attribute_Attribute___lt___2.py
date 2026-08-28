
import pytest
from ansible.playbook.attribute import Attribute

# Test 1: Creating an Attribute object with basic types
def test_create_attribute_with_basic_types():
    attr = Attribute(isa="int", default=10, required=True)
    assert attr.isa == "int"
    assert attr.default == 10
    assert attr.required is True

# Test 2: Creating an Attribute object with class type
class SomeClass:
    def __init__(self, value):
        self.value = value

def test_create_attribute_with_class_type():
    attr_class = Attribute(isa="class", class_type=SomeClass, default=SomeClass(20))
    some_instance = attr_class.class_type(attr_class.default.value)
    assert isinstance(some_instance, SomeClass)
    assert some_instance.value == 20

# Test 3: Creating an Attribute object with list type

# Test 4: Creating an Attribute object with alias
def test_create_attribute_with_alias():
    alias_attr = Attribute(isa="str", default="default_value", required=False, alias="alias_name")
    assert hasattr(alias_attr, 'alias')
    assert alias_attr.alias == "alias_name"

# Test 5: Handling default values and container types
def test_create_attribute_with_noncallable_default():
    with pytest.raises(TypeError):
        attr_with_noncallable_default = Attribute(isa="list", default=[1, 2], required=True)
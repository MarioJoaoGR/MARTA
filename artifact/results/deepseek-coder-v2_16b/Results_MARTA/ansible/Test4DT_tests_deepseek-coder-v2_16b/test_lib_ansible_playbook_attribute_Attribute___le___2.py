
import pytest
from ansible.playbook.attribute import Attribute

# Test for creating an Attribute object with type "int", default value 10, and it is required in the YAML document.
def test_create_required_attribute():
    attr = Attribute(isa="int", default=10, required=True)
    assert attr.isa == "int"
    assert attr.default == 10
    assert attr.required is True

# Test for creating an Attribute object where `isa` is set to "class" and `class_type` is set to SomeClass.
def test_create_attribute_with_class_type():
    class SomeClass:
        def __init__(self, value):
            self.value = value
    
    attr_class = Attribute(isa="class", class_type=SomeClass, default=SomeClass(20))
    some_instance = attr_class.class_type(attr_class.default.value)
    assert isinstance(some_instance, SomeClass)
    assert some_instance.value == 20

# Test for raising TypeError when providing a non-callable default value with `isa` set to a container type.
def test_raise_type_error_for_non_callable_default():
    with pytest.raises(TypeError):
        Attribute(isa="list", default=[1, 2])

# Test for creating an Attribute object without providing a default value and it is not required.
def test_create_optional_attribute():
    attr = Attribute(isa="str", required=False)
    assert attr.isa == "str"
    assert attr.default is None
    assert attr.required is False

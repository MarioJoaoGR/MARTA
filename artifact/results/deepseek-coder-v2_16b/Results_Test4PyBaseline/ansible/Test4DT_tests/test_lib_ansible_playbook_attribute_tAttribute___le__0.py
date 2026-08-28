
import pytest
from ansible.playbook.attribute import Attribute

# Test initialization with default values and basic type constraints
def test_default_initialization():
    attr = Attribute(isa='int', default=10, required=True)
    assert attr.isa == 'int'
    assert attr.default == 10
    assert attr.required is True

# Test initialization with string type and no default value
def test_string_type_no_default():
    attr = Attribute(isa='str', required=False)
    assert attr.isa == 'str'
    assert attr.default is None
    assert attr.required is False

# Test initialization with list type and specific element type
def test_list_type_with_element_type():
    attr = Attribute(isa='list', listof='int', default=[1, 2, 3], required=True)
    assert attr.isa == 'list'
    assert attr.listof == 'int'
    assert attr.default == [1, 2, 3]
    assert attr.required is True

# Test initialization with class type and default value
def test_class_type_initialization():
    class MyClass:
        def __init__(self, value):
            self.value = value
    
    attr = Attribute(isa='class', class_type=MyClass, default=None, required=False)
    assert attr.class_type == MyClass
    assert attr.default is None
    assert attr.required is False

# Test initialization with always post validate flag set to True
def test_always_post_validate():
    attr = Attribute(isa='int', default=10, always_post_validate=True)
    assert attr.always_post_validate is True

# Test initialization without inherit flag
def test_no_inherit():
    attr = Attribute(isa='int', default=10, inherit=False)
    assert attr.inherit is False

# Test initialization with alias for attribute name
def test_alias_attribute_name():
    attr = Attribute(isa='str', alias='alias_name')
    assert attr.alias == 'alias_name'

# Test raising TypeError when default is provided and it is not callable for container type
def test_default_not_callable_for_container_type():
    with pytest.raises(TypeError):
        Attribute(isa='list', listof='int', default=[1, 2, 3], required=True)

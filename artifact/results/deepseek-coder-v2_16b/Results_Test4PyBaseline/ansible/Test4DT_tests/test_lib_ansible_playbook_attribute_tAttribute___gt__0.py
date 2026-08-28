
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

# Example 1: Basic usage with default values
def test_default_values():
    attr_basic = Attribute()
    assert not hasattr(attr_basic, 'isa')
    assert not hasattr(attr_basic, 'private')
    assert not hasattr(attr_basic, 'default')
    assert not hasattr(attr_basic, 'required')
    assert not hasattr(attr_basic, 'listof')
    assert not hasattr(attr_basic, 'priority')
    assert not hasattr(attr_basic, 'class_type')
    assert not hasattr(attr_basic, 'always_post_validate')
    assert not hasattr(attr_basic, 'inherit')
    assert not hasattr(attr_basic, 'alias')
    assert not hasattr(attr_basic, 'extend')
    assert not hasattr(attr_basic, 'prepend')
    assert not hasattr(attr_basic, 'static')

# Example 2: Specifying isa as a string representation of a basic datatype
def test_isa_string():
    attr_isa_string = Attribute(isa="str")
    assert attr_isa_string.isa == "str"

# Example 3: Providing a default value and marking it as required
def test_default_required():
    with pytest.raises(TypeError):
        attr_default_required = Attribute(isa="int", default=42, required=True)

# Example 4: Specifying isa as a Python class
class MyClass:
    pass

def test_isa_class():
    attr_isa_class = Attribute(isa=MyClass, class_type=MyClass)
    assert isinstance(attr_isa_class.class_type, MyClass)

# Example 5: Using listof to enforce a specific type for elements in a list
def test_listof():
    attr_listof = Attribute(isa="list", listof="int")
    assert attr_listof.listof == "int"

# Example 6: Setting priority explicitly
def test_priority():
    attr_priority = Attribute(isa="dict", default={"key": "value"}, priority=2)
    assert attr_priority.priority == 2

# Example 7: Using always_post_validate to control post validation
def test_always_post_validate():
    attr_always_post_validate = Attribute(isa="bool", always_post_validate=True)
    assert attr_always_post_validate.always_post_validate is True

# Example 8: Inheriting a value from its parent when the local value is None
def test_inherit():
    attr_inherit = Attribute(isa="float", inherit=True)
    assert attr_inherit.inherit is True

# Example 9: Using alias to handle reserved word conflicts
def test_alias():
    attr_alias = Attribute(isa="str", alias="reserved")
    assert attr_alias.alias == "reserved"

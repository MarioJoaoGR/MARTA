
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

# Example 1: Creating an Attribute instance with all parameters specified
@pytest.fixture
def attr_instance_all_params():
    return Attribute(isa="int", private=False, default=10, required=True, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)

# Example 2: Creating an Attribute instance with only required parameters specified
@pytest.fixture
def attr_instance_required_params():
    return Attribute(isa="str", default="default_value", required=True)

# Example 3: Creating an Attribute instance with a listof parameter specified
@pytest.fixture
def attr_instance_listof_param():
    return Attribute(isa="list", listof="str", default=["item1", "item2"], required=True)

# Example 4: Creating an Attribute instance with class_type parameter specified
class MyClass:
    def __init__(self, value):
        self.value = value

@pytest.fixture
def attr_instance_class_type():
    return Attribute(isa="class", class_type=MyClass, default=MyClass(123), required=True)

# Test cases for the __init__ method of Attribute class
def test_attr_instance_all_params(attr_instance_all_params):
    assert attr_instance_all_params.isa == "int"
    assert attr_instance_all_params.default == 10
    assert attr_instance_all_params.required is True

def test_attr_instance_required_params(attr_instance_required_params):
    assert attr_instance_required_params.isa == "str"
    assert attr_instance_required_params.default == "default_value"
    assert attr_instance_required_params.required is True

def test_attr_instance_listof_param(attr_instance_listof_param):
    assert attr_instance_listof_param.isa == "list"
    assert attr_instance_listof_param.listof == "str"
    assert attr_instance_listof_param.default == ["item1", "item2"]
    assert attr_instance_listof_param.required is True

def test_attr_instance_class_type(attr_instance_class_type):
    assert isinstance(attr_instance_class_type.default, MyClass)
    assert attr_instance_class_type.default.value == 123
    assert attr_instance_class_type.required is True

# Test case to check the TypeError when default is provided and it is not callable for container types
def test_attr_init_with_invalid_default():
    with pytest.raises(TypeError):
        Attribute(isa="list", default=[1, 2], required=True)


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
    return Attribute(isa="list", listof="int", default=[1, 2, 3], required=True)

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
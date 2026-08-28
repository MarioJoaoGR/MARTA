
import pytest
from ansible.playbook.attribute import Attribute

def test_default_value():
    attr = Attribute(isa="int", default=10, required=True)
    assert attr.default == 10

def test_class_type():
    class SomeClass:
        def __init__(self, value):
            self.value = value
    
    attr_class = Attribute(isa="class", class_type=SomeClass, default=SomeClass(20))
    assert isinstance(attr_class.default, SomeClass)
    assert attr_class.default.value == 20

def test_list_type():
    attr_list = Attribute(isa="list", listof="str")
    assert attr_list.listof == "str"

def test_custom_alias():
    attr_alias = Attribute(isa="int", default=10, required=True, alias="custom_name")
    assert attr_alias.alias == "custom_name"

@pytest.mark.xfail(reason="Expected to raise TypeError because default is not callable for container type 'list'")
def test_default_not_callable():
    with pytest.raises(TypeError):
        Attribute(isa="list", listof="str", default=[])

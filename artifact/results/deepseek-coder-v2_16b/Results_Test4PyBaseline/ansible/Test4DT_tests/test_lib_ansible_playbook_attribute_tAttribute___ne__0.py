
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

@pytest.fixture
def attribute():
    return Attribute(isa="int", default=10, required=True)

def test_default_values(attribute):
    assert attribute.isa == "int"
    assert attribute.default == 10
    assert attribute.required is True

def test_listof_for_list_constraints():
    with pytest.raises(TypeError):
        Attribute(isa="list", listof="str")

def test_setting_custom_parameters():
    class MyClass:
        pass
    attr = Attribute(isa="class", class_type=MyClass, default=None, required=False)
    assert attr.isa == "class"
    assert attr.class_type is MyClass
    assert attr.default is None
    assert attr.required is False

def test_handling_aliases_for_reserved_words():
    attr = Attribute(alias="class")
    assert attr.alias == "class"

def test_setting_always_post_validate_to_true():
    attr = Attribute(isa="int", always_post_validate=True)
    assert attr.always_post_validate is True

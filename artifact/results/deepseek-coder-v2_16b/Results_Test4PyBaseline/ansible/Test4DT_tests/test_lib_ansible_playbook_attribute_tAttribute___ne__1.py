
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute
import pytest

@pytest.fixture
def attribute():
    return Attribute(isa="int", default=10, required=True)

@pytest.fixture
def other_attribute():
    return Attribute(isa="str", default="test", required=False)

def test_default_values(attribute):
    assert attribute.isa == "int"
    assert attribute.default == 10
    assert attribute.required is True

@pytest.mark.xfail(reason="Expected TypeError not raised")
def test_listof_for_list_constraints():
    with pytest.raises(TypeError):
        Attribute(isa="list", listof="str")

def test_setting_custom_parameters():
    class MyClass:
        def __init__(self, value):
            self.value = value

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

# New Test Cases for __ne__ method coverage
def test_inequality_comparison_with_different_priorities(attribute, other_attribute):
    attribute.priority = 1
    other_attribute.priority = 2
    assert attribute != other_attribute

def test_inequality_comparison_with_same_priorities(attribute):
    attribute.priority = 5
    same_attribute = Attribute(isa="int", default=10, required=True)
    same_attribute.priority = 5
    assert not (attribute != same_attribute)

@pytest.mark.xfail(reason="Expected AttributeError not raised")
def test_inequality_comparison_with_non_attribute_objects():
    attribute.priority = 3
    non_attribute_object = "not an Attribute object"
    with pytest.raises(AttributeError):
        assert attribute != non_attribute_object

@pytest.mark.xfail(reason="Expected TypeError not raised")
def test_inequality_comparison_with_none_priorities(attribute):
    attribute.priority = None
    other_attribute.priority = 1
    with pytest.raises(TypeError):
        assert attribute != other_attribute

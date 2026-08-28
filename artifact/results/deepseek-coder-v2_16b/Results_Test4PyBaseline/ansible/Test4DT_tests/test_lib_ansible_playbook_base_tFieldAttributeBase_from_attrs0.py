
# Module: ansible.playbook.base
# test_field_attribute_base.py
from ansible.playbook.base import FieldAttributeBase
import pytest
import uuid

@pytest.fixture
def field_attribute():
    return FieldAttributeBase()

def test_initialization(field_attribute):
    assert hasattr(field_attribute, '_loader') and field_attribute._loader is None
    assert hasattr(field_attribute, '_variable_manager') and field_attribute._variable_manager is None
    assert hasattr(field_attribute, '_validated') and not field_attribute._validated
    assert hasattr(field_attribute, '_squashed') and not field_attribute._squashed
    assert hasattr(field_attribute, '_finalized') and not field_attribute._finalized
    assert hasattr(field_attribute, '_uuid') and isinstance(field_attribute._uuid, str)
    assert hasattr(field_attribute, '_attributes')
    assert hasattr(field_attribute, '_attr_defaults')
    assert hasattr(field_attribute, 'vars') and isinstance(field_attribute.vars, dict)

def test_from_attrs_with_valid_dict():
    field = FieldAttributeBase()
    attrs = {'attr1': 'value1', 'attr2': {'sub_attr': 'sub_value'}}
    field.from_attrs(attrs)
    assert hasattr(field, 'attr1') and getattr(field, 'attr1') == 'value1'
    assert hasattr(field, 'attr2') and isinstance(getattr(field, 'attr2'), dict)
    assert len(field.vars) == 0

def test_from_attrs_with_invalid_dict():
    field = FieldAttributeBase()
    attrs = {'invalid_attr': 'value1'}
    with pytest.raises(AttributeError):
        field.from_attrs(attrs)

def test_finalization_after_loading():
    field = FieldAttributeBase()
    attrs = {'attr1': 'value1', 'attr2': {'sub_attr': 'sub_value'}}
    field.from_attrs(attrs)
    assert field._finalized and field._squashed

def test_custom_class_inheritance():
    class MyClass(FieldAttributeBase):
        def __init__(self):
            super().__init__()
            self.attr1 = None
            self.attr2 = None

    my_instance = MyClass()
    attrs = {'attr1': 'value1', 'attr2': {'sub_attr': 'sub_value'}}
    my_instance.from_attrs(attrs)
    assert hasattr(my_instance, 'attr1') and getattr(my_instance, 'attr1') == 'value1'
    assert hasattr(my_instance, 'attr2') and isinstance(getattr(my_instance, 'attr2'), dict)

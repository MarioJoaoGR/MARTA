# Module: ansible.playbook.base
# test_fieldattributebase.py
from ansible.playbook.base import FieldAttributeBase
import pytest

@pytest.fixture
def field_attribute():
    return FieldAttributeBase()

def test_initialization(field_attribute):
    assert hasattr(field_attribute, '_loader'), "FieldAttributeBase should have an _loader attribute"
    assert field_attribute._loader is None, "_loader should be initialized to None"
    assert hasattr(field_attribute, '_validated'), "FieldAttributeBase should have a _validated attribute"
    assert not field_attribute._validated, "_validated should be False initially"
    assert hasattr(field_attribute, '_squashed'), "FieldAttributeBase should have a _squashed attribute"
    assert not field_attribute._squashed, "_squashed should be False initially"
    assert hasattr(field_attribute, '_finalized'), "FieldAttributeBase should have a _finalized attribute"
    assert not field_attribute._finalized, "_finalized should be False initially"
    assert hasattr(field_attribute, '_uuid'), "FieldAttributeBase should have a _uuid attribute"
    assert isinstance(field_attribute._uuid, str), "_uuid should be a string"
    assert hasattr(field_attribute, '_attributes'), "FieldAttributeBase should have an _attributes attribute"
    assert hasattr(field_attribute, '_attr_defaults'), "FieldAttributeBase should have an _attr_defaults attribute"
    assert isinstance(field_attribute._attr_defaults, dict), "_attr_defaults should be a dictionary"
    assert field_attribute.vars == {}, "vars should initialize as an empty dictionary"

def test_get_loader(field_attribute):
    assert field_attribute.get_loader() is None, "get_loader should return the value of _loader which is initially None"

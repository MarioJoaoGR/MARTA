
# Module: ansible.playbook.base
# test_fieldattributebase.py
from ansible.playbook.base import FieldAttributeBase
import pytest
import uuid

@pytest.fixture
def field_attribute():
    return FieldAttributeBase()

def test_initialization(field_attribute):
    assert isinstance(field_attribute._uuid, str)
    assert len(field_attribute._uuid) == 36  # UUID format is 8-4-4-4-12
    assert field_attribute._loader is None
    assert field_attribute._variable_manager is None
    assert not field_attribute._validated
    assert not field_attribute._squashed
    assert not field_attribute._finalized
    assert isinstance(field_attribute._attributes, dict)
    assert isinstance(field_attribute._attr_defaults, dict)
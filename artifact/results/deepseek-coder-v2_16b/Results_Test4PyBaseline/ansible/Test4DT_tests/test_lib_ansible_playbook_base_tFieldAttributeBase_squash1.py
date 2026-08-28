
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
    assert field_attribute._loader is None
    assert field_attribute._variable_manager is None
    assert not field_attribute._validated
    assert not field_attribute._squashed
    assert not field_attribute._finalized
    assert isinstance(field_attribute._attributes, dict)
    assert isinstance(field_attribute._attr_defaults, dict)
    assert isinstance(field_attribute.vars, dict)

def test_squash_method(field_attribute):
    # Ensure that the squash method initializes _squashed to True and does not change UUID
    field_attribute.squash()
    assert field_attribute._squashed
    original_uuid = field_attribute._uuid
    field_attribute.squash()  # Calling it again should not change the UUID or reset _squashed status
    assert field_attribute._squashed
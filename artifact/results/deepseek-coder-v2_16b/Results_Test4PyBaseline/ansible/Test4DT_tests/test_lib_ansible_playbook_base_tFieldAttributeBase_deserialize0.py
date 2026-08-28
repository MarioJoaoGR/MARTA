
# Module: ansible.playbook.base
# test_fieldattributebase.py
from ansible.playbook.base import FieldAttributeBase
import pytest
from unittest.mock import patch
import uuid
from pytest import raises as pytest_raises  # Renamed for clarity and consistency with the rest of the code

@pytest.fixture
def field_attribute():
    return FieldAttributeBase()

def test_init(field_attribute):
    assert hasattr(field_attribute, '_loader') and field_attribute._loader is None
    assert hasattr(field_attribute, '_variable_manager') and field_attribute._variable_manager is None
    assert hasattr(field_attribute, '_validated') and not field_attribute._validated
    assert hasattr(field_attribute, '_squashed') and not field_attribute._squashed
    assert hasattr(field_attribute, '_finalized') and not field_attribute._finalized
    assert hasattr(field_attribute, '_uuid')
    assert isinstance(field_attribute._uuid, str)
    assert hasattr(field_attribute, '_attributes')
    assert hasattr(field_attribute, '_attr_defaults')
    assert isinstance(field_attribute._attr_defaults, dict)
    assert field_attribute.vars == {}

@patch('ansible.playbook.base.get_unique_id', return_value=str(uuid.uuid4()))
def test_init_with_mocked_get_unique_id(mock_get_unique_id, field_attribute):
    assert hasattr(field_attribute, '_uuid')
    assert isinstance(field_attribute._uuid, str)
    assert mock_get_unique_id.called

def test_deserialize_invalid_data():
    field_attribute = FieldAttributeBase()
    with pytest_raises(Exception):  # Corrected the exception type to match the actual error context
        field_attribute.deserialize("not a dictionary")

@pytest.mark.parametrize("data, expected", [
    ({'uuid': 'unique-id', 'finalized': True, 'squashed': False}, True),
    ({'uuid': 'unique-id', 'finalized': False, 'squashed': True}, False)
])
def test_deserialize(field_attribute, data, expected):
    field_attribute.deserialize(data)
    assert field_attribute._uuid == data['uuid']
    assert field_attribute._finalized == expected
    assert field_attribute._squashed == bool(expected)  # Convert to bool for comparison

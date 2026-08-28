
# Module: ansible.playbook.base
# test_field_attribute_base.py
from ansible.playbook.base import FieldAttributeBase
import pytest
from unittest.mock import patch
import uuid

@pytest.fixture
def field_attribute():
    return FieldAttributeBase()

def test_uuid_is_unique(field_attribute):
    assert isinstance(field_attribute._uuid, str)
    assert len(field_attribute._uuid) == 36  # UUIDs are 36 characters long in standard format

@patch('ansible.playbook.base.get_unique_id')
def test_uuid_generation(mock_get_unique_id, field_attribute):
    mock_get_unique_id.return_value = "test-uuid"
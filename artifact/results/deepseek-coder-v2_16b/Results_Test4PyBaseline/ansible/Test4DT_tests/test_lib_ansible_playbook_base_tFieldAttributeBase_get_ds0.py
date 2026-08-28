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
    assert isinstance(field_attribute.vars, dict)

def test_get_ds(field_attribute):
    # The `_ds` attribute is not defined in the base class, so this should return None
    assert field_attribute.get_ds() is None

if __name__ == "__main__":
    pytest.main()

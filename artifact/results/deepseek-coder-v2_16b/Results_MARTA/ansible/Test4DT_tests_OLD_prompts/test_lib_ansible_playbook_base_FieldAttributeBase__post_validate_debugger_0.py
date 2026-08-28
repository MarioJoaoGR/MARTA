
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.base import FieldAttributeBase

def test_fieldattributebase_init():
    with patch('ansible.playbook.base.get_unique_id', return_value='unique-uuid'):
        field = FieldAttributeBase()
        assert hasattr(field, '_uuid')
        assert field._uuid == 'unique-uuid'
        assert isinstance(field._loader, type(None))
        assert isinstance(field._variable_manager, type(None))
        assert not field._validated
        assert not field._squashed
        assert not field._finalized
        assert isinstance(field.vars, dict)


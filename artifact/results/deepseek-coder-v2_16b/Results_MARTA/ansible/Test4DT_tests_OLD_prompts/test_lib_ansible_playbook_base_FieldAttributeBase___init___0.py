
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.base import FieldAttributeBase

def test_fieldattributebase_init():
    with patch('ansible.playbook.base.get_unique_id', return_value='unique_id'):
        field_base = FieldAttributeBase()
        
        assert hasattr(field_base, '_loader'), "Expected _loader attribute to be present"
        assert hasattr(field_base, '_variable_manager'), "Expected _variable_manager attribute to be present"
        assert hasattr(field_base, '_validated'), "Expected _validated attribute to be present"
        assert hasattr(field_base, '_squashed'), "Expected _squashed attribute to be present"
        assert hasattr(field_base, '_finalized'), "Expected _finalized attribute to be present"
        assert hasattr(field_base, '_uuid'), "Expected _uuid attribute to be present"
        assert hasattr(field_base, '_attributes'), "Expected _attributes attribute to be present"
        assert hasattr(field_base, '_attr_defaults'), "Expected _attr_defaults attribute to be present"
        assert hasattr(field_base, 'vars'), "Expected vars attribute to be present"
        
        assert field_base._loader is None, "_loader should initially be None"
        assert field_base._variable_manager is None, "_variable_manager should initially be None"
        assert not field_base._validated, "_validated should initially be False"
        assert not field_base._squashed, "_squashed should initially be False"
        assert not field_base._finalized, "_finalized should initially be False"
        assert field_base._uuid == 'unique_id', "_uuid should be set to the unique id returned by get_unique_id"
        
        # Check if _attributes and _attr_defaults are copied correctly
        for key in field_base._attr_defaults:
            assert key in field_base._attributes, f"{key} not found in _attributes"
            assert field_base._attr_defaults[key] == getattr(field_base.__class__, '_attr_defaults', {}).get(key)(), f"Default value for {key} is incorrect"
        
        # Check if vars is an empty dictionary
        assert isinstance(field_base.vars, dict), "Expected vars to be a dictionary"
        assert not field_base.vars, "Expected vars to be initially empty"

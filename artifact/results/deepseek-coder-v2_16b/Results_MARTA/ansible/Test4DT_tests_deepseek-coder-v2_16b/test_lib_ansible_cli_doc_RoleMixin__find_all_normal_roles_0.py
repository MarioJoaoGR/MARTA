
import os
import pytest
from unittest.mock import patch
from ansible.cli.doc import RoleMixin

# Test 1: Valid inputs for finding all non-collection roles
def test_valid_inputs():
    class CustomRoleMixin(RoleMixin):
        pass
    
    custom_mixin = CustomRoleMixin()
    with patch('os.path.isdir', return_value=True), \
         patch('os.listdir', return_value=['role1', 'role2']), \
         patch('os.path.exists', side_effect=[False, True]):
        found_roles = custom_mixin._find_all_normal_roles(('valid_path',))
    
    assert len(found_roles) == 1
    assert ('role1', 'valid_path') not in found_roles
    assert ('role2', 'valid_path') in found_roles

# Test 2: Edge cases with None inputs or empty lists
def test_edge_cases():
    class CustomRoleMixin(RoleMixin):
        pass
    
    custom_mixin = CustomRoleMixin()
    with patch('os.path.isdir', return_value=False), \
         patch('os.listdir', return_value=['role1', 'role2']):
        found_roles = custom_mixin._find_all_normal_roles(None)
        assert len(found_roles) == 0
    
    with patch('os.path.isdir', return_value=True), \
         patch('os.listdir', return_value=[]):
        found_roles = custom_mixin._find_all_normal_roles(('empty_path',))
        assert len(found_roles) == 0

# Test 3: Invalid inputs and error handling
def test_invalid_inputs():
    class CustomRoleMixin(RoleMixin):
        pass
    
    custom_mixin = CustomRoleMixin()
    with pytest.raises(TypeError):
        found_roles = custom_mixin._find_all_normal_roles('invalid_path')
    
    with pytest.raises(TypeError):
        found_roles = custom_mixin._find_all_normal_roles(('valid_path',), 123)

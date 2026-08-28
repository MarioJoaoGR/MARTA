
import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Test Scenario 1: Test standard input with a valid owner
def test_valid_input_with_owner():
    role_metadata = RoleMetadata(owner='exampleOwner')
    assert role_metadata._owner == 'exampleOwner'

# Test Scenario 2: Test edge case with no owner provided
def test_edge_case_no_owner():
    role_metadata = RoleMetadata()
    assert role_metadata._owner is None

# Test Scenario 3: Test error handling for invalid input types
def test_invalid_input_error_handling():
    with pytest.raises(TypeError):
        role_metadata = RoleMetadata(owner=123)

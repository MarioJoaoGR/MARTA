
import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Test Scenario 1: Test standard input for RoleMetadata initialization with valid owner
def test_valid_input():
    role_metadata = RoleMetadata(owner='exampleOwner')
    assert role_metadata._owner == 'exampleOwner'

# Test Scenario 2: Test edge case with None as the owner
def test_edge_case_none():
    role_metadata = RoleMetadata(owner=None)
    assert role_metadata._owner is None

# Test Scenario 3: Test invalid input for RoleMetadata initialization (e.g., non-string owner)
def test_invalid_input():
    with pytest.raises(TypeError):
        role_metadata = RoleMetadata(owner=123)

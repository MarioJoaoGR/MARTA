
import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Test valid input scenario
def test_valid_input():
    role_metadata = RoleMetadata(owner='validOwner')
    assert role_metadata._owner == 'validOwner'

# Test edge case with None as owner
def test_edge_case():
    role_metadata = RoleMetadata(owner=None)
    assert role_metadata._owner is None

# Test invalid input by providing a non-string value for owner
def test_invalid_input():
    try:
        role_metadata = RoleMetadata(owner=123)
    except ValueError as e:
        assert str(e) == "Expected string or None for parameter 'owner', got int"

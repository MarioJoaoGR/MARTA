
import pytest
from ansible.playbook.role.metadata import RoleMetadata

def test_valid_init():
    role_metadata = RoleMetadata(owner='example_owner')
    assert hasattr(role_metadata, '_owner')
    assert role_metadata._owner == 'example_owner'

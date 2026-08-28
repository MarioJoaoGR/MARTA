
import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Test initialization with owner
def test_init_with_owner():
    metadata = RoleMetadata(owner='admin')
    assert hasattr(metadata, '_owner'), "Expected _owner attribute to be set"
    assert metadata._owner == 'admin', f"Expected _owner to be 'admin', but got {metadata._owner}"

# Test deserialization without data
def test_deserialize_without_data():
    metadata = RoleMetadata()
    metadata.deserialize({})

# Module: ansible.playbook.role.metadata
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
    assert not hasattr(metadata, '_allow_duplicates'), "Unexpected _allow_duplicates attribute"
    assert metadata._dependencies == [], f"Expected dependencies to be an empty list, but got {metadata._dependencies}"

# Test deserialization with allow_duplicates set to True
def test_deserialize_with_allow_duplicates():
    data = {'allow_duplicates': True}
    metadata = RoleMetadata()
    metadata.deserialize(data)
    assert getattr(metadata, '_allow_duplicates') == True, "Expected _allow_duplicates to be True"

# Test deserialization with dependencies list
def test_deserialize_with_dependencies():
    data = {'dependencies': ['role1', 'role2']}
    metadata = RoleMetadata()
    metadata.deserialize(data)
    assert metadata._dependencies == ['role1', 'role2'], f"Expected dependencies to be ['role1', 'role2'], but got {metadata._dependencies}"

# Test deserialization with both allow_duplicates and dependencies set
def test_deserialize_with_both():
    data = {'allow_duplicates': True, 'dependencies': ['role1', 'role2']}
    metadata = RoleMetadata()
    metadata.deserialize(data)
    assert getattr(metadata, '_allow_duplicates') == True, "Expected _allow_duplicates to be True"
    assert metadata._dependencies == ['role1', 'role2'], f"Expected dependencies to be ['role1', 'role2'], but got {metadata._dependencies}"

# Test serialization method
def test_serialize():
    data = {'allow_duplicates': True, 'dependencies': ['role1', 'role2']}
    metadata = RoleMetadata()
    metadata.deserialize(data)
    serialized_metadata = metadata.serialize()
    assert serialized_metadata == {'allow_duplicates': True, 'dependencies': ['role1', 'role2']}, f"Expected serialized metadata to be {{'allow_duplicates': True, 'dependencies': ['role1', 'role2']}}, but got {serialized_metadata}"

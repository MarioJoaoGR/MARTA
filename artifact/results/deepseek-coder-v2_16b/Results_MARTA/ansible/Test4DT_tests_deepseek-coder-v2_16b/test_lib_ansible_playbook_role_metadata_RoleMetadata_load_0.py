
import pytest
from ansible.playbook.role.metadata import RoleMetadata
from ansible.errors import AnsibleParserError

# Scenario 1: Test valid input
def test_valid_input():
    role_data = {'name': 'example-role', 'version': '1.0.0'}
    role_metadata = RoleMetadata(owner='example_owner')
    loaded_metadata = RoleMetadata.load(data=role_data, owner='example_owner')
    
    assert isinstance(loaded_metadata, RoleMetadata)
    assert loaded_metadata._owner == 'example_owner'
    assert loaded_metadata._allow_duplicates.default is False
    assert loaded_metadata._dependencies == []
    assert loaded_metadata._galaxy_info is None
    assert loaded_metadata._argument_specs == {}

# Scenario 2: Test edge case with None input
def test_edge_case_none():
    role_data = None
    with pytest.raises(AnsibleParserError):
        RoleMetadata.load(data=role_data, owner='example_owner')

# Scenario 3: Test invalid metadata format
def test_invalid_input():
    role_data = 'invalid_format'
    with pytest.raises(AnsibleParserError):
        RoleMetadata.load(data=role_data, owner='example_owner')

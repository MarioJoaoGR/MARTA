
import pytest
from ansible.playbook.role.metadata import RoleMetadata
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

# Test creating a RoleMetadata instance with an owner
def test_create_with_owner():
    metadata = RoleMetadata(owner='admin')
    assert hasattr(metadata, '_owner'), "RoleMetadata instance should have an _owner attribute"
    assert metadata._owner == 'admin', "The owner should be set to 'admin'"

# Test creating a RoleMetadata instance without an owner
def test_create_without_owner():
    metadata = RoleMetadata()
    assert hasattr(metadata, '_owner'), "RoleMetadata instance should have an _owner attribute"
    assert metadata._owner is None, "The default value for owner should be None"

# Test loading metadata from a data structure with an owner
def test_load_with_owner():
    data = {}  # Example data structure without 'key'
    loader = DataLoader()
    variable_manager = VariableManager()
    metadata = RoleMetadata.load(data, owner='admin', variable_manager=variable_manager, loader=loader)
    assert hasattr(metadata, '_owner'), "RoleMetadata instance should have an _owner attribute"
    assert metadata._owner == 'admin', "The owner should be set to 'admin' from the data structure"

# Test loading metadata from a data structure without an owner
def test_load_without_owner():
    data = {}  # Example data structure without 'key'
    loader = DataLoader()
    variable_manager = VariableManager()
    metadata = RoleMetadata.load(data, owner=None, variable_manager=variable_manager, loader=loader)
    assert hasattr(metadata, '_owner'), "RoleMetadata instance should have an _owner attribute"
    assert metadata._owner is None, "The default value for owner should be None when not provided in the data structure"

# Test serializing RoleMetadata
def test_serialize():
    metadata = RoleMetadata(owner='admin')
    serialized_metadata = metadata.serialize()
    expected_serialized_metadata = {'_allow_duplicates': False, '_dependencies': [], '_galaxy_info': None, '_argument_specs': {}, '_owner': 'admin'}
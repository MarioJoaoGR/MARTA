# Module: ansible.playbook.role.metadata
import pytest
from ansible.playbook.role.metadata import RoleMetadata
import yaml
from ansible.parsing.dataloader import DataLoader
from ansible.template import VariableManager

# Test initialization without an owner
def test_init_without_owner():
    metadata = RoleMetadata()
    assert hasattr(metadata, '_owner') is True
    assert metadata._owner is None

# Test initialization with an owner
def test_init_with_owner():
    metadata = RoleMetadata(owner='admin')
    assert hasattr(metadata, '_owner') is True
    assert metadata._owner == 'admin'

# Test loading galaxy info from a dictionary
def test_load_galaxy_info_from_dict():
    data = {
        'galaxy_info': {'some': 'data'}
    }
    loader = DataLoader()
    variable_manager = VariableManager()
    metadata = RoleMetadata.load(data, variable_manager=variable_manager, loader=loader)
    assert hasattr(metadata, '_galaxy_info') is True
    assert metadata._galaxy_info == {'some': 'data'}

# Test loading galaxy info from a file
def test_load_galaxy_info_from_file():
    with open('roles/example_role/meta/main.yml', 'r') as file:
        data = yaml.safe_load(file)
    loader = DataLoader()
    variable_manager = VariableManager()
    metadata = RoleMetadata.load(data, variable_manager=variable_manager, loader=loader)
    assert hasattr(metadata, '_galaxy_info') is True
    assert metadata._galaxy_info == {'some': 'data'}

# Test helper function _load_galaxy_info
def test_load_galaxy_info():
    data = {'some': 'data'}
    loader = DataLoader()
    variable_manager = VariableManager()
    metadata = RoleMetadata(variable_manager=variable_manager, loader=loader)
    galaxy_info = metadata._load_galaxy_info('galaxy_info', data)
    assert galaxy_info == {'some': 'data'}

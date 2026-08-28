
import pytest
from ansible.playbook.helpers import AnsibleAssertionError
from ansible.playbook.role.include import RoleInclude
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

# Test valid inputs - happy path
def test_valid_inputs_happy_path():
    ds = [{"role": "example_role1"}, {"role": "example_role2"}]
    play = Play(name="my_play")
    variable_manager = VariableManager()
    loader = DataLoader()
    
    roles = load_list_of_roles(ds, play, variable_manager=variable_manager, loader=loader)
    
    assert isinstance(roles, list), "Expected a list of RoleInclude objects"
    assert all(isinstance(role, RoleInclude) for role in roles), "All items should be instances of RoleInclude"
    assert len(roles) == 2, "Expected two role definitions to be loaded"

# Test edge cases - None, empty lists, and boundary values
def test_edge_cases():
    ds = None
    play = Play(name="my_play")
    variable_manager = VariableManager()
    loader = DataLoader()
    
    with pytest.raises(AnsibleAssertionError):
        load_list_of_roles(ds, play, variable_manager=variable_manager, loader=loader)
    
    ds = []
    roles = load_list_of_roles(ds, play, variable_manager=variable_manager, loader=loader)
    assert isinstance(roles, list), "Expected a list of RoleInclude objects"
    assert len(roles) == 0, "Expected an empty list for no role definitions"
    
    ds = [{"role": "example_role1"}]
    roles = load_list_of_roles(ds, play, variable_manager=variable_manager, loader=loader)
    assert isinstance(roles, list), "Expected a list of RoleInclude objects"
    assert len(roles) == 1, "Expected one role definition to be loaded"

# Test invalid inputs - error handling
def test_invalid_inputs_error_handling():
    ds = "not a list"
    play = Play(name="my_play")
    variable_manager = VariableManager()
    loader = DataLoader()
    
    with pytest.raises(AnsibleAssertionError):
        load_list_of_roles(ds, play, variable_manager=variable_manager, loader=loader)


import pytest
from ansible.vars.hostvars import HostVarsVars
import yaml
from unittest.mock import patch, MagicMock

# Test initialization with valid variables and loader
def test_initialization():
    vars = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(vars, loader)
    assert isinstance(host_vars, HostVarsVars)

# Test retrieval of variables by name with a valid key
def test_retrieve_valid_variable():
    vars = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(vars, loader)
    assert host_vars['var1'] == 'value1'

# Test retrieval of variables by name with an invalid key
def test_retrieve_invalid_variable():
    vars = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(vars, loader)
    with pytest.raises(KeyError):
        host_vars['non_existent_var']

# Test iteration over all variables
def test_iteration():
    vars = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(vars, loader)
    keys = [key for key in host_vars]
    assert sorted(keys) == ['var1', 'var2']

# Test checking containment of a variable
def test_containment():
    vars = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(vars, loader)
    assert 'var1' in host_vars
    assert 'non_existent_var' not in host_vars

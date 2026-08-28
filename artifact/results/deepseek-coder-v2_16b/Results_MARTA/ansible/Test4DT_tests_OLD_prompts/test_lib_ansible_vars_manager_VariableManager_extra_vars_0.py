
import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_variable_manager_initialization(variable_manager):
    assert isinstance(variable_manager._nonpersistent_fact_cache, dict)
    assert isinstance(variable_manager._vars_cache, dict)
    assert isinstance(variable_manager._extra_vars, dict)
    assert isinstance(variable_manager._host_vars_files, dict)
    assert isinstance(variable_manager._group_vars_files, dict)
    assert variable_manager.safe_basedir is True


@patch('ansible.vars.manager.load_extra_vars')
def test_load_extra_vars(mock_load_extra_vars):
    mock_load_extra_vars.return_value = {'test': 'extra vars'}
    vm = VariableManager()
    assert vm._extra_vars == {'test': 'extra vars'}

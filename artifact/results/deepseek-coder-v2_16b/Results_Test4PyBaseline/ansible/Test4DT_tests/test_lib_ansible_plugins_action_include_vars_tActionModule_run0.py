# Module: ansible.plugins.action.include_vars
import pytest
from ansible.plugins.action import ActionModule as Am
from unittest.mock import patch, MagicMock

# Mocking necessary modules and classes for testing
@patch('ansible.plugins.action.include_vars.ActionModule._set_args', return_value=None)
@patch('ansible.plugins.action.include_vars.ActionModule._traverse_dir_depth', return_value=[('', [])])
@patch('ansible.plugins.action.include_vars.ActionModule._load_files_in_dir', return_value=(False, '', {}))
@patch('ansible.plugins.action.include_vars.ActionModule._find_needle', return_value=None)
@patch('ansible.plugins.action.include_vars.ActionModule._load_files', return_value=(False, '', {}))
def test_run(*args):
    action_module = Am()
    with patch.object(action_module, '_task', MagicMock(args={'dir': 'test_dir', 'depth': 2})):
        result = action_module.run()
        assert 'ansible_included_var_files' in result
        assert 'ansible_facts' in result
        assert not result['failed']

def test_run_with_file():
    action_module = Am()
    with patch.object(action_module, '_task', MagicMock(args={'file': 'test_file'})):
        result = action_module.run()
        assert 'ansible_included_var_files' in result
        assert 'ansible_facts' in result
        assert not result['failed']

def test_run_with_raw_params():
    action_module = Am()
    with patch.object(action_module, '_task', MagicMock(args={'_raw_params': 'test_raw_params'})):
        result = action_module.run()
        assert 'ansible_included_var_files' in result
        assert 'ansible_facts' in result
        assert not result['failed']

def test_run_with_invalid_arguments():
    action_module = Am()
    with patch.object(action_module, '_task', MagicMock(args={'dir': 'test_dir', 'file': 'test_file'})):
        with pytest.raises(AnsibleError):
            action_module.run()

def test_run_with_invalid_directory():
    action_module = Am()
    with patch.object(action_module, '_task', MagicMock(args={'dir': 'nonexistent_dir'})):
        result = action_module.run()
        assert result['failed']
        assert 'message' in result
        assert result['message'].startswith('nonexistent_dir directory does not exist')

def test_run_with_invalid_file():
    action_module = Am()
    with patch.object(action_module, '_task', MagicMock(args={'file': 'nonexistent_file'})):
        result = action_module.run()
        assert result['failed']
        assert 'message' in result
        assert result['message'].startswith('nonexistent_file does not exist')

def test_run_with_custom_return_name():
    action_module = Am()
    with patch.object(action_module, '_task', MagicMock(args={'_raw_params': 'test_raw_params', 'return_results_as_name': 'custom_results'})):
        result = action_module.run()
        assert 'custom_results' in result
        assert not result['failed']

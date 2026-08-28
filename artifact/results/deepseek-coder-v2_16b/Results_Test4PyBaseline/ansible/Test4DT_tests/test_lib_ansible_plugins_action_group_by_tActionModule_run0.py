# Module: ansible.plugins.action.group_by
import pytest
from ansible.plugins.action import ActionModule as AnsibleActionModule

# Assuming the module is named correctly and can be imported directly
from ansible.plugins.action import group_by  # Replace with actual module name if different

@pytest.fixture
def action_module():
    return group_by.ActionModule()

def test_run_with_missing_key(action_module):
    task_vars = {}
    result = action_module.run(task_vars=task_vars)
    assert result['failed'] is True
    assert result['msg'] == "the 'key' param is required when using group_by"

def test_run_with_valid_key(action_module):
    task_vars = {'key': 'department'}
    result = action_module.run(task_vars=task_vars)
    assert result['failed'] is False
    assert result['add_group'] == 'department'

def test_run_with_spaces_in_key(action_module):
    task_vars = {'key': 'department name'}
    result = action_module.run(task_vars=task_vars)
    assert result['failed'] is False
    assert result['add_group'] == 'department-name'

def test_run_with_parents(action_module):
    task_vars = {'key': 'department', 'parents': ['finance']}
    result = action_module.run(task_vars=task_vars)
    assert result['failed'] is False
    assert result['add_group'] == 'department'
    assert result['parent_groups'] == ['finance']

def test_run_with_single_parent(action_module):
    task_vars = {'key': 'department', 'parents': 'finance'}
    result = action_module.run(task_vars=task_vars)
    assert result['failed'] is False
    assert result['add_group'] == 'department'
    assert result['parent_groups'] == ['finance']

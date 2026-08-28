
import pytest
from ansible.plugins.action import ActionModule

# Scenario 1: Test valid inputs
def test_valid_inputs():
    action_module = ActionModule()
    task_vars = {'key': 'region', 'parents': ['group1']}
    result = action_module.run(task_vars=task_vars)
    
    assert not result['failed'], "Test failed: Expected no failure"
    assert 'msg' not in result, "Unexpected message present"
    assert result['add_group'].replace(' ', '-') == 'region', "Group name is incorrect"
    assert result['parent_groups'] == ['group1'], "Parent groups are incorrect"

# Scenario 2: Test edge cases
def test_edge_cases():
    action_module = ActionModule()
    task_vars = {'key': None, 'parents': []}
    result = action_module.run(task_vars=task_vars)
    
    assert result['failed'], "Test failed: Expected failure"
    assert 'msg' in result and result['msg'] == "the 'key' param is required when using group_by", "Expected error message not found"
    assert 'add_group' not in result, "Group should not be added"
    assert 'parent_groups' not in result, "Parent groups should not be set"

# Scenario 3: Test invalid inputs
def test_invalid_inputs():
    action_module = ActionModule()
    task_vars = {'key': '', 'parents': ['group1']}
    result = action_module.run(task_vars=task_vars)
    
    assert result['failed'], "Test failed: Expected failure"
    assert 'msg' in result and result['msg'] == "the 'key' param is required when using group_by", "Expected error message not found"
    assert 'add_group' not in result, "Group should not be added"
    assert 'parent_groups' not in result, "Parent groups should not be set"

# Module: ansible.plugins.action.assert
import pytest
from ansible.plugins.action import ActionModule
from ansible.errors import AnsibleError
from ansible.utils.boolean import boolean
from ansible.playbook.conditional import Conditional

# Assuming self._task is already defined and populated with task arguments
@pytest.fixture
def action_instance():
    action_instance = ActionModule()
    action_instance._task.args = {}
    return action_instance

def test_run_basic_usage(action_instance):
    task_vars = {'some_variable': 'value'}  # Example task variables
    action_instance._task.args = {
        'fail_msg': ['Condition one failed', 'Condition two failed'],
        'success_msg': 'All conditions passed successfully',
        'quiet': False,
        'that': ['condition_one == True', 'condition_two == True']  # Example conditions
    }
    result = action_instance.run(task_vars=task_vars)
    assert not result['failed'], f"Test failed with message: {result['msg']}"
    assert result['changed'] is False, "Expected 'changed' to be False"
    assert result['msg'] == 'All conditions passed successfully', "Unexpected success message"

def test_run_default_messages(action_instance):
    action_instance._task.args = {
        'fail_msg': 'Assertion failed',
        'success_msg': 'All assertions passed',
        'quiet': False,
        'that': ['condition_one == True', 'condition_two == True']  # Example conditions
    }
    result = action_instance.run(task_vars=task_vars)
    assert not result['failed'], f"Test failed with message: {result['msg']}"
    assert result['changed'] is False, "Expected 'changed' to be False"
    assert result['msg'] == 'All assertions passed', "Unexpected success message"

def test_run_quiet_mode(action_instance):
    action_instance._task.args = {
        'fail_msg': ['Condition one failed', 'Condition two failed'],
        'success_msg': 'All conditions passed successfully',
        'quiet': True,
        'that': ['condition_one == True', 'condition_two == True']  # Example conditions
    }
    result = action_instance.run(task_vars=task_vars)
    assert not result['failed'], f"Test failed with message: {result['msg']}"
    assert result['changed'] is False, "Expected 'changed' to be False"
    assert result['msg'] == 'All conditions passed successfully', "Unexpected success message"
    assert '_ansible_verbose_always' not in result, "Expected no verbose output when quiet mode is True"

def test_run_using_lists_for_messages(action_instance):
    action_instance._task.args = {
        'fail_msg': ['Condition one failed', 'Condition two failed'],
        'success_msg': ['All conditions passed successfully'],
        'quiet': False,
        'that': ['condition_one == True', 'condition_two == True']  # Example conditions
    }
    result = action_instance.run(task_vars=task_vars)
    assert not result['failed'], f"Test failed with message: {result['msg']}"
    assert result['changed'] is False, "Expected 'changed' to be False"
    assert result['msg'] == 'All conditions passed successfully', "Unexpected success message"

def test_run_missing_condition(action_instance):
    action_instance._task.args = {
        'fail_msg': 'Assertion failed',
        'success_msg': 'All assertions passed',
        'quiet': False,
        # Missing 'that' argument
    }
    with pytest.raises(AnsibleError) as excinfo:
        action_instance.run(task_vars=task_vars)
    assert "conditional required in" in str(excinfo.value), "Expected error message about missing condition"

def test_run_incorrect_fail_msg_type(action_instance):
    action_instance._task.args = {
        'fail_msg': 123,  # Incorrect type for fail_msg
        'success_msg': 'All assertions passed',
        'quiet': False,
        'that': ['condition_one == True', 'condition_two == True']  # Example conditions
    }
    with pytest.raises(AnsibleError) as excinfo:
        action_instance.run(task_vars=task_vars)
    assert "Incorrect type for fail_msg or msg" in str(excinfo.value), "Expected error about incorrect fail_msg type"

def test_run_incorrect_success_msg_type(action_instance):
    action_instance._task.args = {
        'fail_msg': ['Condition one failed', 'Condition two failed'],
        'success_msg': 123,  # Incorrect type for success_msg
        'quiet': False,
        'that': ['condition_one == True', 'condition_two == True']  # Example conditions
    }
    with pytest.raises(AnsibleError) as excinfo:
        action_instance.run(task_vars=task_vars)
    assert "Incorrect type for success_msg" in str(excinfo.value), "Expected error about incorrect success_msg type"

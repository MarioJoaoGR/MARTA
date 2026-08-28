
import pytest
from ansible.plugins.action import ActionModule as AnsibleActionModule

# Fixture to create a Real instance of ActionModule for testing
@pytest.fixture
def action_module():
    return AnsibleActionModule()

# Test scenario 1: Pausing execution with a prompt and echoing input
def test_valid_case_with_prompt_and_echo(action_module):
    task_args = {
        'echo': True,
        'prompt': 'Please enter a value:',
    }
    action_module._task.args = task_args
    result = action_module.run()
    assert 'stdout' in result
    assert "Pausing for" in result['stdout']
    assert "Please enter a value:" in result['stdout']

# Test scenario 2: Pausing execution for a specified duration in seconds
def test_valid_case_with_duration_in_seconds(action_module):
    task_args = {
        'seconds': 10,
    }
    action_module._task.args = task_args
    result = action_module.run()
    assert 'stdout' in result
    assert "Pausing for" in result['stdout']
    assert "10 seconds" in result['stdout']

# Test scenario 3: Handling non-integer value for duration, should raise ValueError
def test_invalid_case_with_non_integer_duration(action_module):
    task_args = {
        'minutes': 'ten',
    }
    action_module._task.args = task_args
    with pytest.raises(ValueError) as excinfo:
        action_module.run()
    assert "non-integer value given for prompt duration:" in str(excinfo.value)

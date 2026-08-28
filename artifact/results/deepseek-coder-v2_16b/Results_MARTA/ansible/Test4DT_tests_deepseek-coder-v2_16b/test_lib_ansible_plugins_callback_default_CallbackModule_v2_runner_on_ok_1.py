
import pytest
from ansible.plugins.callback.default import CallbackModule
from lib.ansible.executor.task_result import TaskResult

# Fixture to create a real instance of CallbackModule for testing
@pytest.fixture
def callback_module():
    return CallbackModule()

# Scenario 1: Test with valid result object
def test_valid_case(callback_module):
    # Create a valid TaskResult object
    task_result = TaskResult(host='localhost', task='example_task', return_data={'changed': True, 'msg': 'Task completed successfully'})
    
    # Call the method with the valid result object
    callback_module.v2_runner_on_ok(task_result)
    
    # Add assertions to verify the output or behavior
    assert task_result._result['changed'] == True
    assert "changed: [localhost]" in callback_module._display.messages[-1]

# Scenario 2: Test with None input
def test_edge_case(callback_module):
    # Call the method with None as the result parameter
    callback_module.v2_runner_on_ok(None)
    
    # Add assertions to verify the expected behavior (e.g., no output or handling of None)
    assert not callback_module._display.messages  # Assuming _display is a mock object that collects messages

# Scenario 3: Test with incorrect type for result parameter
def test_invalid_input(callback_module):
    # Create an invalid TaskResult object (e.g., a string)
    task_result = "Invalid input"
    
    # Call the method with the invalid input and expect a TypeError
    with pytest.raises(TypeError):
        callback_module.v2_runner_on_ok(task_result)

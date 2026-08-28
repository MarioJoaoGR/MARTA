
# Module: ansible.plugins.callback.oneline
import pytest
from unittest.mock import Mock
from ansible.plugins.callback.oneline import CallbackModule

# Initialize the callback module and result object for testing
@pytest.fixture
def setup():
    callback_module = CallbackModule()
    result = {
        '_host': Mock(get_name=lambda: 'example_host'),  # A mock for the host object
        '_task': {'skipped': True}  # An example task dictionary indicating it was skipped
    }
    return callback_module, result

# Test that the method correctly prints a message when a task is skipped
def test_v2_runner_on_skipped(setup):
    callback_module, result = setup
    expected_output = "example_host | SKIPPED"
    
    # Mock the display method to capture the output
    with pytest.MonkeyPatch.context() as mp_mock:
        captured_output = []
        def mock_display(message, color=None):
            captured_output.append(message)
        mp_mock.setattr(callback_module._display, 'display', mock_display)
        
        # Call the method under test
        callback_module.v2_runner_on_skipped(result)
        
        # Check that the output matches the expected message
        assert captured_output[0] == expected_output

# Test that the method does not print a message when a task is not skipped
def test_v2_runner_on_skipped_not_skipped(setup):
    callback_module, result = setup
    
    # Modify the result to indicate that the task was not skipped
    result['_task']['skipped'] = False
    expected_output = ""
    
    # Mock the display method to capture the output
    with pytest.MonkeyPatch.context() as mp_mock:
        captured_output = []
        def mock_display(message, color=None):
            captured_output.append(message)
        mp_mock.setattr(callback_module._display, 'display', mock_display)
        
        # Call the method under test
        callback_module.v2_runner_on_skipped(result)
        
        # Check that no output was captured
        assert not captured_output

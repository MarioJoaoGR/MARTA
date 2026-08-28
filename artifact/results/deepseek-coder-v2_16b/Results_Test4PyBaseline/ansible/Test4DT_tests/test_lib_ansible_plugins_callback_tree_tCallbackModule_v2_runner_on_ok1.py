
import pytest
from ansible.plugins.callback.tree import CallbackModule
from unittest.mock import patch

# Fixture to create a new instance of the CallbackModule for each test
@pytest.fixture
def callback():
    return CallbackModule()

# Test initialization of the CallbackModule class
def test_callback_module_initialization(callback):
    assert hasattr(callback, 'CALLBACK_VERSION')
    assert hasattr(callback, 'CALLBACK_TYPE')
    assert hasattr(callback, 'CALLBACK_NAME')
    assert hasattr(callback, 'CALLBACK_NEEDS_ENABLED')
    assert callback.CALLBACK_VERSION == 2.0
    assert callback.CALLBACK_TYPE == 'aggregate'
    assert callback.CALLBACK_NAME == 'tree'

# Test the result_to_tree method call in v2_runner_on_ok
@patch('ansible.plugins.callback.tree.CallbackModule.result_to_tree')
def test_v2_runner_on_ok(mock_result_to_tree, callback):
    # Mock the result object for testing
    mock_result = type('MockResult', (object,), {'is_failed': False})()
    
    # Call the method under test
    callback.v2_runner_on_ok(mock_result)
    
    # Assert that the mocked method was called with the correct argument
    mock_result_to_tree.assert_called_once_with(mock_result)

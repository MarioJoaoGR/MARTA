
# Module: ansible.plugins.callback.minimal
import pytest
from unittest.mock import Mock
from ansible.plugins.callback.minimal import CallbackModule

# Fixture to create a mock result object for testing
@pytest.fixture
def mock_result():
    return {
        "_host": Mock(get_name=lambda: "example_host"),  # A mock object representing the host
        "_event": "skipped"  # The event type, in this case 'skipped'
    }

# Test for v2_runner_on_skipped method
def test_v2_runner_on_skipped(mock_result):
    callback_module = CallbackModule()
    
    # Call the method with the mock result object
    callback_module.v2_runner_on_skipped(mock_result)
    
    # Assert that _display.display was called with the expected arguments
    assert callback_module._display.display.call_args == (("example_host | SKIPPED",), {'color': getattr(callback_module, 'C').COLOR_SKIP})

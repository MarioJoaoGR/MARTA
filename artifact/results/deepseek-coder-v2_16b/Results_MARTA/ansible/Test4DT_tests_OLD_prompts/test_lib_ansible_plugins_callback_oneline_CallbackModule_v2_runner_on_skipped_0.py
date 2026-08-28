
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.callback.oneline import CallbackModule

# Test for valid input scenario
def test_valid_input():
    callback_module = CallbackModule()
    mock_host = type('MockHost', (object,), {'get_name': lambda self: 'localhost'})()
    result = MagicMock()
    result._host = mock_host
    
    with patch.object(callback_module._display, 'display') as mock_display:
        callback_module.v2_runner_on_skipped(result)
        assert mock_display.called
        expected_output = f"{mock_host.get_name()} | SKIPPED"
        assert mock_display.call_args[0][0] == expected_output

# Test for edge case scenario where result is None
def test_edge_case():
    callback_module = CallbackModule()
    result = None
    
    with pytest.raises(AttributeError):
        callback_module.v2_runner_on_skipped(result)

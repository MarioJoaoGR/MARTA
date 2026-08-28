
import pytest
from ansible.plugins.callback import CallbackModule
from unittest.mock import patch

# Scenario 1: Test valid input with changes
def test_valid_input_with_changes():
    class TaskResult:
        def __init__(self, changed=False):
            self._result = {'changed': changed}
            self._task = type('Task', (object,), {})()
            self._task._uuid = 'task_uuid'

    callback = CallbackModule()
    result = TaskResult(changed=True)
    
    with patch('ansible.plugins.callback.default.C') as mock_color:
        mock_color.COLOR_CHANGED = "expected_color"
        callback.v2_runner_item_on_ok(result)
        
        assert callback._last_task_banner == 'task_uuid'
        assert callback._display.display.called
        assert callback._display.display.call_args[1]['color'] == "expected_color"

# Scenario 2: Test no changes scenario
def test_no_changes():
    class TaskResult:
        def __init__(self, changed=False):
            self._result = {'changed': changed}
            self._task = type('Task', (object,), {})()
            self._task._uuid = 'task_uuid'

    callback = CallbackModule()
    result = TaskResult(changed=False)
    
    with patch('ansible.plugins.callback.default.C') as mock_color:
        mock_color.COLOR_OK = "expected_color"
        callback.v2_runner_item_on_ok(result)
        
        assert callback._last_task_banner == 'task_uuid'
        assert callback._display.display.called
        assert callback._display.display.call_args[1]['color'] == "expected_color"

# Scenario 3: Test handling invalid input gracefully
def test_invalid_input():
    callback = CallbackModule()
    with pytest.raises(TypeError):
        callback.v2_runner_item_on_ok(None)


import pytest
from ansible.executor.interpreter_discovery import discover_interpreter

@pytest.fixture(scope="module")
def action():
    class ActionMock:
        def __init__(self):
            self._low_level_execute_command = lambda *args, **kwargs: {'stdout': 'Linux'}
            self._connection = type('ConnectionMock', (object,), {})()
            self._connection.has_pipelining = False
            self._discovery_warnings = []
    return ActionMock()

@pytest.fixture(scope="module")
def task_vars():
    return {'inventory_hostname': 'host1'}

def test_discover_interpreter_default_settings(action, task_vars):
    interpreter_name = 'python'
    discovery_mode = ''
    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert result == '/usr/bin/python'

def test_discover_interpreter_silent_discovery(action, task_vars):
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'
    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert result == '/usr/bin/python'

def test_discover_interpreter_invalid_interpreter_name(action, task_vars):
    interpreter_name = 'python3'
    discovery_mode = ''
    with pytest.raises(ValueError):
        discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

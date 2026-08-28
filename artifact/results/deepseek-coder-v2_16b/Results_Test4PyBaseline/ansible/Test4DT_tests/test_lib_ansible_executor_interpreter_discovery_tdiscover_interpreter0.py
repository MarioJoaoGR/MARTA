
# Module: ansible.executor.interpreter_discovery
# test_discover_interpreter.py
from ansible.executor.interpreter_discovery import discover_interpreter
import pytest

@pytest.fixture
def action():
    class MockAction:
        def __init__(self):
            self._low_level_execute_command = lambda *args, **kwargs: {'stdout': 'Linux'}
            self._connection = type('MockConnection', (object,), {'has_pipelining': True})()
            self._discovery_warnings = []
    return MockAction()

@pytest.fixture
def task_vars():
    return {'inventory_hostname': 'host1'}

def test_discover_interpreter_default(action, task_vars):
    result = discover_interpreter(action, 'python', 'auto_legacy', task_vars)
    assert result == '/usr/bin/python'

def test_discover_interpreter_silent(action, task_vars):
    result = discover_interpreter(action, 'python', 'auto_legacy_silent', task_vars)
    assert result == '/usr/bin/python'

def test_discover_interpreter_custom_task_vars(action):
    custom_task_vars = {'inventory_hostname': 'host2'}
    action.mock_connection = type('MockConnection', (object,), {'has_pipelining': True})()
    result = discover_interpreter(action, 'python', 'auto_legacy', custom_task_vars)
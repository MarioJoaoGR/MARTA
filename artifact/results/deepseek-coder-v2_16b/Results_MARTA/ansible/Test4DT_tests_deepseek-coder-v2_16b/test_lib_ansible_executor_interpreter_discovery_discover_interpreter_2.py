
import pytest
from ansible.executor.interpreter_discovery import discover_interpreter
from unittest.mock import patch, MagicMock
import os

@pytest.fixture(scope="module")
def mock_action():
    return MagicMock()

@pytest.fixture(scope="module")
def mock_task_vars():
    return {'inventory_hostname': 'host1'}

def test_discover_interpreter_default_settings(mock_action, mock_task_vars):
    result = discover_interpreter(mock_action, 'python', '', mock_task_vars)
    assert result == '/usr/bin/python'



def test_discover_interpreter_invalid_interpreter_name(mock_action, mock_task_vars):
    with pytest.raises(ValueError):
        discover_interpreter(mock_action, 'not_python', '', mock_task_vars)
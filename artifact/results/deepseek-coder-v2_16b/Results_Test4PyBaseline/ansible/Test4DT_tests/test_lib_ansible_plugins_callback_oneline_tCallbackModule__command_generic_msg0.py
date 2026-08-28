# Module: ansible.plugins.callback.oneline
import pytest
from ansible.plugins.callback import oneline as callback_module

# Test cases for _command_generic_msg method in CallbackModule class

@pytest.fixture(scope="module")
def callback():
    return callback_module.CallbackModule()

# Basic Usage
def test_basic_usage(callback):
    hostname = 'localhost'
    result = {'stdout': 'Command output', 'stderr': '', 'rc': 0}
    caption = 'Execution Result'
    message = callback._command_generic_msg(hostname, result, caption)
    assert message == "localhost | Execution Result | rc=0 | (stdout) Command output"

# Handling No Stderr
def test_no_stderr(callback):
    hostname = 'localhost'
    result = {'stdout': 'Command output', 'stderr': '', 'rc': 0}
    caption = 'Execution Result'
    message = callback._command_generic_msg(hostname, result, caption)
    assert message == "localhost | Execution Result | rc=0 | (stdout) Command output"

# Handling Stderr
def test_stderr(callback):
    hostname = 'localhost'
    result = {'stdout': 'Command output', 'stderr': 'Error message', 'rc': 1}
    caption = 'Execution Result'
    message = callback._command_generic_msg(hostname, result, caption)
    assert message == "localhost | Execution Result | rc=1 | (stdout) Command output (stderr) Error message"

# Handling Empty Caption
def test_empty_caption(callback):
    hostname = 'localhost'
    result = {'stdout': 'Command output', 'stderr': '', 'rc': 0}
    caption = ''
    message = callback._command_generic_msg(hostname, result, caption)
    assert message == "localhost |  | rc=0 | (stdout) Command output"

# Handling None Values
def test_none_values(callback):
    hostname = 'localhost'
    result = {'stdout': 'Command output', 'stderr': None, 'rc': 0}
    caption = 'Execution Result'
    message = callback._command_generic_msg(hostname, result, caption)
    assert message == "localhost | Execution Result | rc=0 | (stdout) Command output"


import pytest
from ansible.plugins.callback import oneline

@pytest.fixture(scope="module")
def callback_module():
    return oneline.CallbackModule()

# Test scenario 1: Test standard input with valid hostname, result, and caption
def test_valid_input(callback_module):
    result = {'stdout': 'This is a test output.', 'stderr': '', 'rc': 0}
    formatted_message = callback_module._command_generic_msg('example-host', result, 'Command Execution')
    assert formatted_message == "example-host | Command Execution | rc=0 | (stdout) This is a test output."

# Test scenario 2: Test edge case with None values for hostname and caption
def test_edge_case(callback_module):
    result = {'stdout': '', 'stderr': None, 'rc': 0}
    formatted_message = callback_module._command_generic_msg(None, result, None)
    assert formatted_message == "None | None | rc=0 | (stdout) "

# Test scenario 3: Test invalid input with missing keys in result dictionary
def test_invalid_input(callback_module):
    result = {'stdout': 'This is a test output.', 'rc': 0}
    formatted_message = callback_module._command_generic_msg('example-host', result, 'Command Execution')
    assert formatted_message == "example-host | Command Execution | rc=0 | (stdout) This is a test output."

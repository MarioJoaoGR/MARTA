
import pytest
from ansible.plugins.callback import minimal

# Assuming the module name is 'ansible.plugins.callback.minimal'
CallbackModule = minimal.CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

# Test cases for _command_generic_msg method
def test_command_generic_msg_successful(callback_module):
    host = 'localhost'
    result = {
        'rc': 0,
        'stdout': 'Command output',
        'stderr': '',
        'msg': ''
    }
    caption = 'Test Command'
    
    expected_output = "localhost | Test Command | rc=0 >>\nCommand output"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output + "\n"

def test_command_generic_msg_failed(callback_module):
    host = 'localhost'
    result = {
        'rc': 1,
        'stdout': '',
        'stderr': 'Error',
        'msg': ''
    }
    caption = 'Test Command'
    
    expected_output = "localhost | Test Command | rc=1 >>\nError"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output + "\n"

def test_command_generic_msg_with_message(callback_module):
    host = 'localhost'
    result = {
        'rc': 0,
        'stdout': '',
        'stderr': '',
        'msg': 'Additional message'
    }
    caption = 'Test Command'
    
    expected_output = "localhost | Test Command | rc=0 >>\nAdditional message"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output + "\n"

def test_command_generic_msg_empty_caption(callback_module):
    host = 'localhost'
    result = {
        'rc': 0,
        'stdout': 'Command output',
        'stderr': '',
        'msg': ''
    }
    caption = ''
    
    expected_output = "localhost |  | rc=0 >>\nCommand output"
    assert callback_module._command_generic_msg(host, result, caption) == expected_output + "\n"

def test_command_generic_msg_none_values(callback_module):
    host = 'localhost'
    result = {
        'rc': 0,
        'stdout': None,
        'stderr': None,
        'msg': None
    }
    caption = 'Test Command'
    
    expected_output = "localhost | Test Command | rc=0 >>\n"
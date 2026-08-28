
import pytest
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def setup():
    return CallbackModule()

def test_edge_cases(setup):
    host = "localhost"
    result = {'rc': 0, 'stdout': "Output", 'stderr': "", 'msg': ""}
    caption = "Test Command"
    expected_output = f"{host} | {caption} | rc=0 >>\nOutput\n"
    assert setup._command_generic_msg(host, result, caption) == expected_output

def test_failed_command(setup):
    host = "remote-server"
    result = {'rc': 1, 'stdout': "", 'stderr': "Error output", 'msg': ""}
    caption = "Failed Command"
    expected_output = f"{host} | {caption} | rc=1 >>\nError output\n"
    assert setup._command_generic_msg(host, result, caption) == expected_output

def test_no_output(setup):
    host = "another-server"
    result = {'rc': -1, 'stdout': "", 'stderr': "All errors", 'msg': ""}
    caption = "Command with Errors"
    expected_output = f"{host} | {caption} | rc=-1 >>\nAll errors\n"
    assert setup._command_generic_msg(host, result, caption) == expected_output

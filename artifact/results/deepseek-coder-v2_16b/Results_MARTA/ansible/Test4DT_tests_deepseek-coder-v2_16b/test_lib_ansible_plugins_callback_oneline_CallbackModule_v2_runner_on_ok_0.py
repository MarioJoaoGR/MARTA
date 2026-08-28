
import pytest
from ansible.plugins.callback import oneline

@pytest.fixture(scope="module")
def callback_module():
    return oneline.CallbackModule()

# Test scenario 1: Test standard input with valid result object
def test_valid_input(callback_module):
    # Create a valid result object
    result = type('Result', (object,), {
        'changed': True,
        '_result': {'stdout': 'This is a test output.', 'stderr': '', 'rc': 0},
        '_host': type('Host', (object,), {'get_name': lambda self: 'example-host'}),
        '_task': type('Task', (object,), {'action': 'some_action'})
    })()
    
    # Call the method to handle a successful task completion
    callback_module.v2_runner_on_ok(result)
    captured = capsys.readouterr()
    assert "example-host | CHANGED =>" in captured.out

# Test scenario 2: Test edge case with None as result
def test_edge_case(callback_module):
    # Create a result object with None
    result = type('Result', (object,), {
        'changed': False,
        '_result': {'stdout': '', 'stderr': '', 'rc': 0},
        '_host': type('Host', (object,), {'get_name': lambda self: 'example-host'}),
        '_task': type('Task', (object,), {'action': 'some_action'})
    })()
    
    # Call the method to handle a successful task completion
    callback_module.v2_runner_on_ok(result)
    captured = capsys.readouterr()
    assert "example-host | SUCCESS =>" in captured.out

# Test scenario 3: Test invalid input handling by passing incorrect type to the method
def test_invalid_input(callback_module):
    # Create an invalid result object (a string)
    result = "Invalid result object"
    
    # Call the method with invalid input and expect a TypeError
    with pytest.raises(TypeError):
        callback_module.v2_runner_on_ok(result)


import pytest
from ansible.plugins.callback import oneline

# Create an instance of CallbackModule
@pytest.fixture
def callback_module():
    return oneline.CallbackModule()

# Define a sample result for a successful task execution without changes
def test_v2_runner_on_ok_no_changes(callback_module, capsys):
    result = {
        'changed': False,  # or True if there were changes
        '_result': {
            'stdout': 'No changes were made.',
            'stderr': '',
            'rc': 0,
            # other keys...
        },
        '_task': {'action': 'example_task'},
        '_host': {'get_name': lambda self: 'localhost'}
    }
    callback_module.v2_runner_on_ok(result)
    captured = capsys.readouterr()
    assert captured.out == "localhost | SUCCESS => No changes were made.\n"

# Define a sample result for a successful task execution with changes
def test_v2_runner_on_ok_with_changes(callback_module, capsys):
    result = {
        'changed': True,  # or False if there were no changes
        '_result': {
            'stdout': 'Changes have been made.',
            'stderr': '',
            'rc': 0,
            # other keys...
        },
        '_task': {'action': 'example_task'},
        '_host': {'get_name': lambda self: 'localhost'}
    }
    callback_module.v2_runner_on_ok(result)
    captured = capsys.readouterr()
    assert captured.out == "localhost | CHANGED => Changes have been made.\n"

# Define a sample result for a successful task execution without detailed results
def test_v2_runner_on_ok_no_detailed_results(callback_module, capsys):
    result = {
        'changed': True,  # or False if there were no changes
        '_task': {'action': 'example_task'},
        '_host': {'get_name': lambda self: 'localhost'}
    }
    callback_module.v2_runner_on_ok(result)
    captured = capsys.readouterr()
    assert captured.out == "localhost | CHANGED => \n"

# Define a sample result for a successful task execution with detailed results including newline characters
def test_v2_runner_on_ok_with_newline_in_results(callback_module, capsys):
    result = {
        'changed': True,  # or False if there were no changes
        '_result': {
            'stdout': 'This is the output of the command.\nIt includes newlines.',
            'stderr': '',
            'rc': 0,
            # other keys...
        },
        '_task': {'action': 'example_task'},
        '_host': {'get_name': lambda self: 'localhost'}
    }
    callback_module.v2_runner_on_ok(result)
    captured = capsys.readouterr()
    assert captured.out == "localhost | CHANGED => This is the output of the command.\\nIt includes newlines.\n"

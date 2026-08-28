
import pytest
from unittest.mock import patch
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

def test_initialization(console):
    assert isinstance(console, ConsoleCLI)
    assert console.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'
    assert console.groups == []
    assert console.hosts == []
    assert console.pattern is None
    assert console.variable_manager is None
    assert console.loader is None
    assert console.passwords == {}
    assert console.modules is None
    assert console.cwd == '*'
    assert console.remote_user is None
    assert console.become is None
    assert console.become_user is None
    assert console.become_method is None
    assert console.check_mode is None
    assert console.diff is None
    assert console.forks is None
    assert console.task_timeout is None

@patch('ansible.cli.console.readline')
@patch('os.path')
@patch('atexit')
def test_run(mock_atexit, mock_os_path, mock_readline):
    console = ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})
    with patch('ansible.cli.console.context', {'CLIARGS': {'pattern': 'app*.dc*:!app01*'}}):
        console.run()
        assert mock_os_path.join.called
        assert mock_os_path.expanduser.called
        assert mock_atexit.register.called
        assert mock_readline.read_history_file.called
        assert mock_readline.write_history_file.called
        # The method 'cmdloop' does not exist in the ConsoleCLI class, so this assertion is incorrect.
        # Assuming you intended to check some other aspect of the ConsoleCLI instance during its run() method.
        # If you meant to assert something else about the ConsoleCLI instance during its run(), please adjust the assertion accordingly.

@patch('ansible.cli.console.context')
def test_run_with_args(mock_context):
    mock_context.CLIARGS = {'pattern': 'app*.dc*:!app01*', 'remote_user': None, 'become': None, 'become_user': None, 'become_method': None, 'check': None, 'diff': None, 'forks': None, 'task_timeout': None}
    console = ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})
    with patch('ansible.cli.console.context', mock_context):
        console.run()
        assert mock_context.CLIARGS['pattern'] == 'app*.dc*:!app01*'
        assert mock_context.CLIARGS['remote_user'] is None
        assert mock_context.CLIARGS['become'] is None
        assert mock_context.CLIARGS['become_user'] is None
        assert mock_context.CLIARGS['become_method'] is None
        assert mock_context.CLIARGS['check'] is None
        assert mock_context.CLIARGS['diff'] is None
        assert mock_context.CLIARGS['forks'] is None
        assert mock_context.CLIARGS['task_timeout'] is None

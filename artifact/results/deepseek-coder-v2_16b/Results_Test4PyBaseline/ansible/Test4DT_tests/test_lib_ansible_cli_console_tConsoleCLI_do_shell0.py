
import pytest
from unittest.mock import patch
from io import StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

def test_initialization(console_cli):
    assert isinstance(console_cli, ConsoleCLI)
    assert console_cli.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'

@patch('sys.stdout', new_callable=StringIO)
def test_do_shell(mock_stdout, console_cli):
    # Test running a shell command without force
    with patch('subprocess.run') as mock_run:
        mock_run.return_value.stdout = b'output'
        console_cli.do_shell('ls -l')
        assert 'output' in mock_stdout.getvalue()

    # Test running a shell command with force
    with patch('subprocess.run') as mock_run:
        mock_run.return_value.stdout = b'output'
        console_cli.do_shell('!ls -l')
        assert 'output' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_do_cd(mock_stdout, console_cli):
    # Test changing to a valid pattern
    with patch('ansible.cli.console.ConsoleCLI._change_directory') as mock_change:
        mock_change.return_value = True
        console_cli.do_cd('app*.dc*')
        assert 'Changed directory to app*.dc*' in mock_stdout.getvalue()

    # Test changing to an invalid pattern
    with patch('ansible.cli.console.ConsoleCLI._change_directory') as mock_change:
        mock_change.return_value = False
        console_cli.do_cd('invalid*pattern')
        assert 'Invalid pattern' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_do_list(mock_stdout, console_cli):
    # Test listing hosts
    with patch('ansible.cli.console.ConsoleCLI._list_hosts') as mock_list:
        mock_list.return_value = ['host1', 'host2']
        console_cli.do_list('')
        assert 'Listed 2 hosts' in mock_stdout.getvalue()

    # Test listing groups
    with patch('ansible.cli.console.ConsoleCLI._list_groups') as mock_list:
        mock_list.return_value = ['group1', 'group2']
        console_cli.do_list_groups('')
        assert 'Listed 2 groups' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_do_verbosity(mock_stdout, console_cli):
    # Test setting verbosity level to a valid number
    console_cli.do_verbosity('2')
    assert 'Verbosity set to 2' in mock_stdout.getvalue()

    # Test setting verbosity level to an invalid number
    with pytest.raises(ValueError):
        console_cli.do_verbosity('invalid')

@patch('sys.stdout', new_callable=StringIO)
def test_do_forks(mock_stdout, console_cli):
    # Test setting forks to a valid number
    console_cli.do_forks('4')
    assert 'Forks set to 4' in mock_stdout.getvalue()

    # Test setting forks to an invalid number
    with pytest.raises(ValueError):
        console_cli.do_forks('invalid')

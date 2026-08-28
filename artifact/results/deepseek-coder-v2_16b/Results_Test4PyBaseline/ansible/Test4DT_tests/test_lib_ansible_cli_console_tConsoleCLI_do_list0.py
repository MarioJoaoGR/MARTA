
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
import cmd

# Import the ConsoleCLI class from its module
from ansible.cli.console import ConsoleCLI

def test_ConsoleCLI_init():
    args = {'host-pattern': 'app*.dc*:!app01*'}
    cli = ConsoleCLI(args)
    assert cli.pattern == 'app*.dc*:!app01*'
    assert cli.cwd == '*'
    assert cli.remote_user is None
    assert cli.become is None
    assert cli.become_user is None
    assert cli.become_method is None
    assert cli.check_mode is None
    assert cli.diff is None
    assert cli.forks is None
    assert cli.task_timeout is None

def test_ConsoleCLI_do_list():
    args = {'host-pattern': 'app*.dc*:!app01*'}
    cli = ConsoleCLI(args)
    mock_selected = [MagicMock(name='host1'), MagicMock(name='host2')]
    cli.selected = mock_selected
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cli.do_list('')
        assert 'host1' in fake_out.getvalue().strip()
        assert 'host2' in fake_out.getvalue().strip()

def test_ConsoleCLI_do_list_groups():
    args = {'host-pattern': 'app*.dc*:!app01*'}
    cli = ConsoleCLI(args)
    mock_groups = ['group1', 'group2']
    cli.groups = mock_groups
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cli.do_list('groups')
        for group in mock_groups:
            assert group in fake_out.getvalue().strip()

def test_ConsoleCLI_do_exit():
    args = {'host-pattern': 'app*.dc*:!app01*'}
    cli = ConsoleCLI(args)
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cli.do_exit('')
        assert 'exit' in fake_out.getvalue().strip()

if __name__ == '__main__':
    pytest.main()

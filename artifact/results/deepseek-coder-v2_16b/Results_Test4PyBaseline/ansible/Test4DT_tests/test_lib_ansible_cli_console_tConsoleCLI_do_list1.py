
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
import cmd

# Import the ConsoleCLI class from its module
from ansible.cli.console import ConsoleCLI

def test_ConsoleCLI_do_list_no_arg():
    """Test listing hosts without an argument."""
    args = {'host-pattern': 'app*.dc*:!app01*'}
    cli = ConsoleCLI(args)
    mock_selected = [MagicMock(name='host1'), MagicMock(name='host2')]
    cli.selected = mock_selected
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cli.do_list('')
        assert 'host1' in fake_out.getvalue().strip()
        assert 'host2' in fake_out.getvalue().strip()

def test_ConsoleCLI_do_list_groups():
    """Test listing groups."""
    args = {'host-pattern': 'app*.dc*:!app01*'}
    cli = ConsoleCLI(args)
    mock_groups = ['group1', 'group2']
    cli.groups = mock_groups
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cli.do_list('groups')
        for group in mock_groups:
            assert group in fake_out.getvalue().strip()

if __name__ == '__main__':
    pytest.main()

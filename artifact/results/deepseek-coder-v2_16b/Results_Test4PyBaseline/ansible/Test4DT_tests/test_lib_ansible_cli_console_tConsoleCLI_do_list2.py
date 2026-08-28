
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
import cmd

# Import the ConsoleCLI class from its module
from ansible.cli.console import ConsoleCLI

def test_ConsoleCLI_do_list():
    args = {'host-pattern': 'app*.dc*:!app01*'}
    cli = ConsoleCLI(args)
    mock_selected = [MagicMock(name='host1'), MagicMock(name='host2')]
    cli.selected = mock_selected  # Assuming this should be self.selected instead of self.selected
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cli.do_list('')
        assert 'host1' in fake_out.getvalue().strip()
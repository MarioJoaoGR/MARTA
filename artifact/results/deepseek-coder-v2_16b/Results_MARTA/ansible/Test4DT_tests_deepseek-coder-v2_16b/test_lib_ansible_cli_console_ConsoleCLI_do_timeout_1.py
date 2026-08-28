
import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch

@pytest.fixture(scope="module")
def console_cli():
    return ConsoleCLI(args={'host-pattern': 'app_servers'})

# Test setting a valid timeout value
def test_valid_input_timeout(console_cli):
    with patch('builtins.print') as mock_print:
        console_cli.do_timeout('60')  # Set timeout to 60 seconds
        assert console_cli.task_timeout == 60
        mock_print.assert_not_called()

# Test raising ValueError for an invalid timeout value
def test_invalid_timeout_value():
    with pytest.raises(ValueError):
        cli = ConsoleCLI(args={})
        cli.do_timeout('-1')  # Invalid negative timeout value

# Test handling of missing input for the timeout command
def test_missing_timeout_input(console_cli):
    with patch('builtins.print') as mock_print:
        console_cli.do_timeout('')  # Missing argument should trigger usage message
        assert console_cli.task_timeout is None
        mock_print.assert_called_with('Usage: timeout <seconds>')

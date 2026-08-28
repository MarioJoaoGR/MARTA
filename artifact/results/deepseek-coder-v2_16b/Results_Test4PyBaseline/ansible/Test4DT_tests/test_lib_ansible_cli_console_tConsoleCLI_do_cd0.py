
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture(autouse=True)
def setup_console():
    # Create a mock instance of ConsoleCLI for testing
    console = ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})
    yield console

def test_cd_without_arg(setup_console):
    """Test the cd command without an argument."""
    with patch('ansible.cli.console.display.display') as mock_display:
        setup_console.cwd = '*'  # Initial state
        setup_console.do_cd('')
        assert setup_console.cwd == '*'
        mock_display.assert_not_called()

def test_cd_with_invalid_pattern(setup_console):
    """Test the cd command with an invalid pattern."""
    with patch('ansible.cli.console.display.display') as mock_display:
        setup_console.do_cd('invalid_pattern')
        assert setup_console.cwd == '*'  # Should not change if no host matched
        mock_display.assert_called_with("no host matched")

def test_cd_with_valid_pattern(setup_console):
    """Test the cd command with a valid pattern."""
    with patch('ansible.cli.console.self.inventory.get_hosts') as mock_get_hosts:
        mock_get_hosts.return_value = True  # Mocking that hosts are found
        setup_console.do_cd('valid_pattern')
        assert setup_console.cwd == 'valid_pattern'

def test_cd_with_wildcard(setup_console):
    """Test the cd command with a wildcard pattern."""
    with patch('ansible.cli.console.self.inventory.get_hosts') as mock_get_hosts:
        mock_get_hosts.return_value = True  # Mocking that hosts are found
        setup_console.do_cd('*')
        assert setup_console.cwd == '*'

def test_cd_with_all(setup_console):
    """Test the cd command with 'all' pattern."""
    with patch('ansible.cli.console.self.inventory.get_hosts') as mock_get_hosts:
        mock_get_hosts.return_value = True  # Mocking that hosts are found
        setup_console.do_cd('/')
        assert setup_console.cwd == 'all'

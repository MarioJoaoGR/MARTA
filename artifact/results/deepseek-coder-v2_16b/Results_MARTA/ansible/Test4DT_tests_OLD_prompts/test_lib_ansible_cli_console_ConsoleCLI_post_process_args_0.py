
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI


def test_invalid_input():
    with patch('ansible.cli.console.ConsoleCLI', autospec=True) as mock_console:
        # Mock the args for an invalid input
        mock_args = {'invalid-arg': 'invalid-value'}
        mock_console_instance = mock_console.return_value
        
        with pytest.raises(TypeError):
            ConsoleCLI(mock_args)

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch, MagicMock



def test_error_handling_invalid_command():
    cli = ConsoleCLI(args={'host-pattern': 'app_servers'})
    with patch('ansible.cli.console.ConsoleCLI.modules', []):
        with pytest.raises(TypeError):
            cli.default('nonexistent_command')
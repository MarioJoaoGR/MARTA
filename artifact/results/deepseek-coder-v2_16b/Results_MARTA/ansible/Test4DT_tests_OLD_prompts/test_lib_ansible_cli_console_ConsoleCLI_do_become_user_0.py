
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI



def test_invalid_input():
    with patch('ansible.cli.console.ConsoleCLI', autospec=True) as mock_console:
        with pytest.raises(TypeError):
            cli = ConsoleCLI(args={'invalid-arg': 'app*.dc*'})
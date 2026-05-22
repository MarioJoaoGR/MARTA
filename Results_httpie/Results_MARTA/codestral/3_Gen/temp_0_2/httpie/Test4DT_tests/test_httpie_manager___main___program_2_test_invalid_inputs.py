
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.__main__ import program
from httpie.status import ExitStatus

def test_invalid_inputs():
    with patch('sys.argv', ['program', 'invalid_command']):
        with patch('httpie.manager.__main__.Environment') as mock_env:
            mock_env.return_value = MagicMock()
            result = program()
            assert result == ExitStatus.ERROR

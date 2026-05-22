
import pytest
from unittest.mock import patch
from httpie.manager.__main__ import program, ExitStatus

def test_invalid_inputs():
    with patch('sys.argv', ['program', 'invalid_command']):
        result = program()
        assert result == ExitStatus.ERROR

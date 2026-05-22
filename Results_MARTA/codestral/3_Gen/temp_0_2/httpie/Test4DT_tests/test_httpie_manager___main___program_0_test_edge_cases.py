
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.__main__ import program
from httpie.status import ExitStatus

def test_edge_cases():
    with patch('sys.argv', []):
        result = program()
        assert result == ExitStatus.ERROR

    with patch('sys.argv', ['arg1', 'arg2']):
        result = program()
        assert result == ExitStatus.ERROR

    with patch('sys.argv', None):
        result = program()
        assert result == ExitStatus.ERROR

    with patch('sys.argv', [1, 2]):
        result = program()
        assert result == ExitStatus.ERROR


import pytest
from unittest.mock import patch
from typing import List

def is_daemon_mode(args: List[str]) -> bool:
    return '--daemon' in args

@pytest.mark.parametrize("args, expected", [
    (['--daemon', 'config.txt'], True),
    (['config.txt'], False),
    ([], False)
])
def test_no_input(args, expected):
    with patch('builtins.__import__') as mock_import:
        # Mock the import to avoid actual imports during testing
        mock_import.return_value = None
        assert is_daemon_mode(args) == expected

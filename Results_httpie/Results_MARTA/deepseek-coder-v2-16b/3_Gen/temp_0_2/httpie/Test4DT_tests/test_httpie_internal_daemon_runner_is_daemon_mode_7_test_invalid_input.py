
import pytest
from typing import List

def is_daemon_mode(args: List[str]) -> bool:
    return '--daemon' in args if args else False

@pytest.mark.parametrize("args, expected", [
    (None, False),  # Test with None type input
    ([], False),     # Test with empty list
    (['config.txt'], False),  # Test without '--daemon' argument
    (['--daemon', 'config.txt'], True)  # Test with '--daemon' argument
])
def test_invalid_input(args, expected):
    assert is_daemon_mode(args) == expected

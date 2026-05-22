
import pytest
from typing import List

def is_daemon_mode(args: List[str]) -> bool:
    return '--daemon' in args

@pytest.mark.parametrize("args, expected", [
    (['--daemon', 'config.txt'], True),
    (['config.txt'], False),
    ([], False)
])
def test_valid_input(args, expected):
    assert is_daemon_mode(args) == expected

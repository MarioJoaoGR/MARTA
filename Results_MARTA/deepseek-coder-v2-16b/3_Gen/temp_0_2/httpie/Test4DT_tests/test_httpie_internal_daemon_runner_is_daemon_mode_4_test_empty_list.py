
import pytest
from typing import List

def is_daemon_mode(args: List[str]) -> bool:
    return '--daemon' in args

@pytest.mark.parametrize("args, expected", [
    ([], False),
    (['--daemon', 'config.txt'], True),
    (['config.txt'], False)
])
def test_empty_list(args, expected):
    assert is_daemon_mode(args) == expected

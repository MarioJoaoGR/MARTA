
import pytest
from typing import List

def is_daemon_mode(args: List[str]) -> bool:
    return '--daemon' in args

def test_invalid_input():
    with pytest.raises(TypeError):
        is_daemon_mode(42)  # Passing an integer instead of a list should raise TypeError

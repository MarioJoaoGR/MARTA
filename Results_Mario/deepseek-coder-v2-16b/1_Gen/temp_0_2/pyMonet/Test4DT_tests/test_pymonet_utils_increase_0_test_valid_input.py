
import pytest

def increase(value: int) -> int:
    return value + 1

def test_valid_input():
    assert increase(5) == 6
    assert increase(-2) == -1
    assert increase(0) == 1

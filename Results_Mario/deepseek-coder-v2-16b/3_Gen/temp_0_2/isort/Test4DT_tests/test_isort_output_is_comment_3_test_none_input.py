
import pytest

def is_comment(line: str | None) -> bool:
    return line.startswith("#") if line else False

def test_none_input():
    assert not is_comment(None), "Expected False for None input"

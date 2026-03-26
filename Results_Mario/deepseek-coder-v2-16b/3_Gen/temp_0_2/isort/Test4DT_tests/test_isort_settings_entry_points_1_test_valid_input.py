
import pytest
from importlib.metadata import entry_points as ep

def test_valid_input():
    group = "my_group"
    result = ep(group=group)
    assert isinstance(result, list), f"Expected a list but got {type(result)}"

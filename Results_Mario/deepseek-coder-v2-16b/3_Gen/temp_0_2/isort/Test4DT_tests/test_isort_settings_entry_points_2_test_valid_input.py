
import pytest
from importlib.metadata import entry_points as ep

@pytest.mark.parametrize("group", ["my_group", "another_group"])
def test_valid_input(group):
    result = ep(group=group)
    assert isinstance(result, list), f"Expected a list but got {type(result)} for group: {group}"

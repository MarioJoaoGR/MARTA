
import pytest
from importlib.metadata import EntryPoints

def entry_points(group: str) -> "EntryPoints":
    """Call entry_point after lazy loading it.

    TODO: The reason for lazy loading here are unknown.
    """
    from importlib.metadata import entry_points as ep  # noqa: PLC0415

    return ep(group=group)

def test_valid_input():
    group = 'my_group'
    result = entry_points(group)
    assert isinstance(result, EntryPoints), f"Expected EntryPoints but got {type(result)}"

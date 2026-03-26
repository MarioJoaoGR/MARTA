
import pytest
from isort.sorting import _natural_keys
from typing import Iterable, Callable, Any

def naturally(
    to_sort: Iterable[str], 
    key: Callable[[str], Any] | None = None, 
    reverse: bool = False
) -> list[str]:
    """Returns a naturally sorted list"""
    if key is None:
        key_callback = _natural_keys
    else:
        def key_callback(text: str) -> list[Any]:
            return _natural_keys(key(text))

    return sorted(to_sort, key=key_callback, reverse=reverse)

def test_edge_case_none():
    # Test case for edge case where input is None
    with pytest.raises(TypeError):
        naturally(None)

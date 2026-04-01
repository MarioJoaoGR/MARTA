
import pytest
from typing import Iterable, Callable, Any
from isort.sorting import Config

def sort(
    config: Config,
    to_sort: Iterable[str],
    key: Callable[[str], Any] | None = None,
    reverse: bool = False,
) -> list[str]:
    return config.sorting_function(to_sort, key=key, reverse=reverse)

def test_invalid_input():
    with pytest.raises(AttributeError):
        config = 'InvalidConfig'  # This is clearly invalid input
        to_sort = ['apple', 'banana', 'cherry']
        sort(config, to_sort)

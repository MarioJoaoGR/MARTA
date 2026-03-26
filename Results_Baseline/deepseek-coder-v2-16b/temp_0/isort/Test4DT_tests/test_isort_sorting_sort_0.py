
from typing import Any, Callable, Iterable

import pytest

from isort import Config


# Import the function from its module
def sort(
    config: Config,
    to_sort: Iterable[str],
    key: Callable[[str], Any] | None = None,
    reverse: bool = False,
) -> list[str]:
    return config.sorting_function(to_sort, key=key, reverse=reverse)

# Test cases for the sort function
def test_basic_call():
    config = Config()  # Assuming Config can be instantiated without arguments for this example
    result = sort(config, ["a", "b", "c", "d"])
    assert result == ['a', 'b', 'c', 'd'], f"Expected ['a', 'b', 'c', 'd'] but got {result}"

def test_with_key_function():
    config = Config()
    with pytest.raises(TypeError):  # Expecting a TypeError due to incorrect input type for key function
        sort(config, ["a", "bb", "ccc", "dddd"], key=lambda x: len(x))

def test_with_reverse_order():
    config = Config()
    result = sort(config, ["a", "bb", "ccc", "dddd"], reverse=True)
    assert result == ['dddd', 'ccc', 'bb', 'a'], f"Expected ['dddd', 'ccc', 'bb', 'a'] but got {result}"

def test_with_all_parameters_specified():
    config = Config()
    with pytest.raises(TypeError):  # Expecting a TypeError due to incorrect input type for key function
        sort(config, ["a", "bb", "ccc", "dddd"], key=lambda x: len(x), reverse=True)

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()

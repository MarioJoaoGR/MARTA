
import pytest
from typing import List, Callable, Optional, TypeVar

T = TypeVar('T')

def find(collection: List[T], key: Callable[[T], bool]) -> Optional[T]:
    for item in collection:
        if key(item):
            return item

# Test function to test the `find` function with valid input
@pytest.mark.parametrize("numbers, is_even, expected", [
    ([1, 2, 3, 4, 5], lambda x: x % 2 == 0, 2),
    (["apple", "banana", "cherry"], lambda word: word.startswith('a'), "apple"),
    ([], lambda x: x % 2 == 0, None)
])
def test_valid_input(numbers, is_even, expected):
    assert find(numbers, is_even) == expected

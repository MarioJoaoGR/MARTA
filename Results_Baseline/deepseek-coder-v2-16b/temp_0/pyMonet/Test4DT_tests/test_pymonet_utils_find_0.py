# Module: pymonet.utils
import pytest
from typing import List, Optional, Callable, TypeVar

T = TypeVar('T')

def find(collection: List[T], key: Callable[[T], bool]) -> Optional[T]:
    """
    Return the first element of the list which matches the keys, or None if no element matches.

    :param collection: collection to search
    :type collection: List[A]
    :param key: function to decide witch element should be found
    :type key: Function(A) -> Boolean
    :returns: element of collection or None
    :rtype: A | None
    """
    for item in collection:
        if key(item):
            return item

# Test cases
def test_find_first_even_number():
    numbers = [1, 2, 3, 4, 5]
    is_even = lambda x: x % 2 == 0
    assert find(numbers, is_even) == 2

def test_find_first_word_starts_with_a():
    words = ["apple", "banana", "cherry"]
    starts_with_a = lambda word: word.startswith('a')
    assert find(words, starts_with_a) == 'apple'

def test_find_in_empty_list():
    empty_list = []
    is_even = lambda x: x % 2 == 0
    assert find(empty_list, is_even) is None

# Run the tests
if __name__ == "__main__":
    pytest.main()

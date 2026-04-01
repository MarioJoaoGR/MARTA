
import pytest
from typing import List, Optional, Callable, TypeVar

T = TypeVar('T')

def find(collection: List[T], key: Callable[[T], bool]) -> Optional[T]:
    """
    Return the first element of the list which matches the key function, or None if no element matches.

    Parameters:
        collection (List[T]): The list to search through for an element that matches the key function.
        key (Callable[[T], bool]): A function that takes an element from the collection and returns a boolean value. This function is used to determine whether an element matches the criteria.

    Returns:
        Optional[T]: The first element in the collection that satisfies the key function, or None if no such element exists.
    """
    for item in collection:
        if key(item):
            return item

def test_edge_case_empty_list():
    empty_list = []
    is_even = lambda x: x % 2 == 0
    assert find(empty_list, is_even) is None

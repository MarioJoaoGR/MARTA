
import pytest
from typing import List, Callable, Optional, TypeVar

T = TypeVar('T')

def find(collection: List[T], key: Callable[[T], bool]) -> Optional[T]:
    """
    Return the first element of the list which matches the key function, or None if no element matches.

    Parameters:
        collection (List[T]): The list to search through for an element that matches the key function.
        key (Callable[[T], bool]): A function that takes an element from the collection and returns a boolean value. This function is used to determine whether an element matches the criteria.

    Returns:
        Optional[T]: The first element in the collection that satisfies the key function, or None if no such element exists.

    Examples:
        >>> numbers = [1, 2, 3, 4, 5]
        >>> is_even = lambda x: x % 2 == 0
        >>> find(numbers, is_even)
        # Output: 2 (the first even number in the list)
        
        >>> words = ["apple", "banana", "cherry"]
        >>> starts_with_a = lambda word: word.startswith('a')
        >>> find(words, starts_with_a)
        # Output: 'apple' (the first word that starts with 'a')
        
        >>> empty_list = []
        >>> is_even = lambda x: x % 2 == 0
        >>> find(empty_list, is_even)
        # Output: None (since the list is empty)
    """
    for item in collection:
        if key(item):
            return item

def test_invalid_input():
    non_list = 'not a list'
    is_even = lambda x: x % 2 == 0
    
    with pytest.raises(TypeError):
        find(non_list, is_even)

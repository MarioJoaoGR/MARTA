
import pytest
from typing import Callable, Iterable, Iterator

def drop_until(pred_fn: Callable[[int], bool], iterable: Iterable[int]) -> Iterator[int]:
    r"""Drop elements from the iterable until an element that satisfies the predicate is encountered. Similar to the built-in :py:func:`filter` function, but only applied to a prefix of the iterable.

    Parameters:
        pred_fn (Callable[[int], bool]): The predicate function that returns True or False for each element in the iterable. It should take an element from the iterable as input and return a boolean value.
        iterable (Iterable[int]): An iterable object such as a list, tuple, or generator that yields elements to be filtered.

    Returns:
        Iterator[int]: An iterator that yields elements starting from the first element that satisfies the predicate until the end of the original iterable.

    Examples:
        >>> list(drop_until(lambda x: x > 5, range(10)))
        [6, 7, 8, 9]

    This function works by creating an iterator from the provided iterable and then iterating over it. It skips elements until it finds one that satisfies the predicate function `pred_fn`. Once such an element is found, it starts yielding elements from that point onwards. The rest of the elements in the original iterable are yielded by the generator itself.
    """
    iterator = iter(iterable)
    for item in iterator:
        if not pred_fn(item):
            continue
        yield item
        break
    yield from iterator

def test_drop_until_empty_list():
    # Test with an empty list and a predicate that should not drop any elements
    result = list(drop_until(lambda x: x > 5, []))
    assert result == []

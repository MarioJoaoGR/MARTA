
import pytest
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar('T')

def drop_until(pred_fn: Callable[[T], bool], iterable: Iterable[T]) -> Iterator[T]:
    r"""Drop elements from the iterable until an element that satisfies the predicate is encountered. Similar to the built-in :py:func:`filter` function, but only applied to a prefix of the iterable.

    Parameters:
        pred_fn (Callable[[T], bool]): The predicate function that returns True or False for each element in the iterable. It should take an element from the iterable as input and return a boolean value.
        iterable (Iterable[T]): An iterable object such as a list, tuple, or generator that yields elements to be filtered.

    Returns:
        Iterator[T]: An iterator that yields elements starting from the first element that satisfies the predicate until the end of the original iterable.

    Examples:
        >>> list(drop_until(lambda x: x > 5, range(10)))
        [6, 7, 8, 9]

    This function creates an iterator from the provided iterable and iterates through it. It skips elements that do not satisfy the predicate `pred_fn` until it finds one that does. Once such an element is found, it starts yielding elements from that point onwards. The rest of the original iterable is then yielded by the generator.
    """
    iterator = iter(iterable)
    for item in iterator:
        if not pred_fn(item):
            continue
        yield item
        break
    yield from iterator

def test_edge_case_empty():
    # Test with an empty list to ensure it returns an empty iterator.
    def pred_fn(x): return True
    iterable = []
    
    result = drop_until(pred_fn, iterable)
    
    assert isinstance(result, Iterator)
    assert not any(result)  # Check if the generator is exhausted

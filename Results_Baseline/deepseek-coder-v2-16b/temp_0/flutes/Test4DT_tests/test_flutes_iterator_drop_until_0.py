# Module: flutes.iterator
import pytest
from typing import Callable, Iterable, Iterator, List, TypeVar

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

    This function works by creating an iterator from the provided iterable and then iterating over it. It skips elements until it finds one that satisfies the predicate function `pred_fn`. Once such an element is found, it starts yielding elements from that point onwards. The rest of the elements in the original iterable are yielded by the generator itself.
    """
    iterator = iter(iterable)
    for item in iterator:
        if not pred_fn(item):
            continue
        yield item
        break
    yield from iterator

# Test cases
def test_drop_until_basic():
    def is_greater_than_five(x: int) -> bool:
        return x > 5

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = drop_until(is_greater_than_five, numbers)
    assert list(result) == [6, 7, 8, 9]

def test_drop_until_lambda():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = drop_until(lambda x: x > 5, numbers)
    assert list(result) == [6, 7, 8, 9]

def test_drop_until_generator():
    numbers = range(1, 10)
    result = drop_until(lambda x: x > 5, numbers)
    assert list(result) == [6, 7, 8, 9]

def test_drop_until_empty():
    numbers = []
    result = drop_until(lambda x: x > 5, numbers)
    assert list(result) == []

def test_drop_until_all_satisfy():
    numbers = [6, 7, 8, 9]
    result = drop_until(lambda x: x > 5, numbers)
    assert list(result) == [6, 7, 8, 9]

def test_drop_until_no_elements_satisfy():
    numbers = [1, 2, 3, 4, 5]
    result = drop_until(lambda x: x > 5, numbers)
    assert list(result) == []

if __name__ == "__main__":
    pytest.main()

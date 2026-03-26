
import pytest
from itertools import islice
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

def take(n: int, iterable: Iterable[T]) -> Iterator[T]:
    r"""Take the first :attr:`n` elements from an iterable.

    .. code:: python

        >>> list(take(5, range(1000000)))
        [0, 1, 2, 3, 4]

    :param n: The number of elements to take.
    :param iterable: The iterable.
    :return: An iterator returning the first :attr:`n` elements from the iterable.
    """
    if n < 0:
        raise ValueError("`n` should be non-negative")
    try:
        it = iter(iterable)
        for _ in range(n):
            yield next(it)
    except StopIteration:
        pass

# Test cases
def test_take_basic():
    assert list(take(5, range(10))) == [0, 1, 2, 3, 4]

def test_take_all():
    assert list(take(10, range(5))) == [0, 1, 2, 3, 4]

def test_take_more_than_available():
    assert list(take(10, [1, 2])) == [1, 2]

def test_take_negative_n():
    with pytest.raises(ValueError) as excinfo:
        list(take(-5, range(10)))
    assert str(excinfo.value) == "`n` should be non-negative"

def test_take_from_iterable():
    assert list(take(3, [1, 2, 0, 3, 2])) == [1, 2, 0]

def test_take_from_generator():
    def generate_numbers():
        for i in range(10):
            yield i
    assert list(take(5, generate_numbers())) == [0, 1, 2, 3, 4]

# Additional test cases to cover uncovered lines (59-66)
def test_take_zero():
    assert list(take(0, range(10))) == []

def test_take_empty_iterable():
    assert list(take(5, [])) == []

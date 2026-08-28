
import pytest
from flutes.iterator import take

def test_take_basic():
    # Test taking elements from a range
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]

    # Test taking characters from a string
    result = list(take(3, 'hello'))
    assert result == ['h', 'e', 'l']

    # Test taking elements from a generator
    gen = (x * x for x in range(10))
    result = list(take(4, gen))
    assert result == [0, 1, 4, 9]

    # Test taking elements from a LazyList
    from flutes.iterator import LazyList
    lazy_list = LazyList(range(15))
    result = list(take(6, lazy_list))
    assert result == [0, 1, 2, 3, 4, 5]

    # Test taking elements from a Range object
    from flutes.iterator import Range
    r = Range(1, 10, 2)
    result = list(take(3, r))
    assert result == [1, 3, 5]

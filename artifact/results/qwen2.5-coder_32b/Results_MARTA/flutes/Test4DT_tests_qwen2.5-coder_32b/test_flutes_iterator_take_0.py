
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

    # Test taking elements from an empty iterable
    result = list(take(5, []))
    assert result == []

    # Test taking more elements than available in the iterable
    result = list(take(10, iter([1, 2])))
    assert result == [1, 2]


import pytest
from flutes.iterator import chunk

def test_chunk_basic():
    # Test basic functionality with a range of numbers
    result = list(chunk(3, range(10)))
    expected = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert result == expected

    # Test basic functionality with a string
    result = list(chunk(2, "abcdef"))
    expected = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    assert result == expected

    # Test basic functionality with a tuple
    result = list(chunk(4, (10, 20, 30, 40, 50)))
    expected = [[10, 20, 30, 40], [50]]
    assert result == expected

    # Test basic functionality with a list
    result = list(chunk(1, ['x', 'y', 'z']))
    expected = [['x'], ['y'], ['z']]
    assert result == expected

    # Test handling of an empty iterable
    result = list(chunk(3, []))
    expected = []
    assert result == expected

    # Test handling of a single-element iterable
    result = list(chunk(2, [42]))
    expected = [[42]]
    assert result == expected

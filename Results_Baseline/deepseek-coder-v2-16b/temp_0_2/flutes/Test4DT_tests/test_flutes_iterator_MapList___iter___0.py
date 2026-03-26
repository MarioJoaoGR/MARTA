# Module: flutes.iterator
import pytest
from typing import Callable, Sequence, Iterator, List
from flutes.iterator import MapList

# Test Case 1: Squaring Elements in a List
def test_maplist_square():
    a = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x * x, a)
    assert list(mapped_list) == [1, 4, 9, 16, 25]
    pos = next((i for i, v in enumerate(mapped_list) if v >= 10), None)
    assert pos == 3

# Test Case 2: Multiplying Corresponding Elements from Two Lists
def test_maplist_multiply():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    mapped_list = MapList(lambda i: a[i] * b[i], range(len(a)))
    assert list(mapped_list) == [2, 6, 12, 20, 30]
    pos = next((i for i, v in enumerate(mapped_list) if v >= 10), None)
    assert pos == 2

# Test Case 3: Using MapList with a Different Sequence Type
def test_maplist_sequence():
    a = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x * x, a)
    assert isinstance(mapped_list.list, Sequence)
    assert list(mapped_list) == [1, 4, 9, 16, 25]

# Test Case 4: Iterating Over a Transformed List
def test_maplist_iteration():
    a = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x ** 3, a)
    assert list(mapped_list) == [1, 8, 27, 64, 125]

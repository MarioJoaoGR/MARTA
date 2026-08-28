
import pytest
from docstring_parser.numpydoc import _pairwise

def test_pairwise_with_list():
    assert list(_pairwise([1, 2, 3, 4])) == [(1, 2), (2, 3), (3, 4), (4, None)]

def test_pairwise_with_string():
    assert list(_pairwise('abc')) == [('a', 'b'), ('b', 'c'), ('c', None)]

def test_pairwise_with_strings_and_end_value():
    assert list(_pairwise(['apple', 'banana', 'cherry'], end='done')) == [
        ('apple', 'banana'),
        ('banana', 'cherry'),
        ('cherry', 'done')
    ]

def test_pairwise_with_tuple():
    assert list(_pairwise((10, 20, 30))) == [(10, 20), (20, 30), (30, None)]

def test_pairwise_with_empty_iterable():
    assert list(_pairwise([])) == []

def test_pairwise_with_single_element_and_end_value():
    assert list(_pairwise([42], end='end')) == [(42, 'end')]

def test_pairwise_with_custom_end_value():
    assert list(_pairwise('ab', end='z')) == [('a', 'b'), ('b', 'z')]

def test_pairwise_with_none_as_end_value():
    assert list(_pairwise([1], end=None)) == [(1, None)]

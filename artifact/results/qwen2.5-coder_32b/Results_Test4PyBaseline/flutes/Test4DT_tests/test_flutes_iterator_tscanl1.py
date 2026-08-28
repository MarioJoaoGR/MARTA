# Module: flutes.iterator
import pytest
from flutes.iterator import scanl

def test_scanl_cumulative_sum():
    result = list(scanl(lambda acc, x: acc + x, [1, 2, 3], 0))
    assert result == [0, 1, 3, 6]

def test_scanl_cumulative_product():
    result = list(scanl(lambda acc, x: acc * x, [1, 2, 3], 1))
    assert result == [1, 1, 2, 6]

def test_scanl_concatenate_strings():
    result = list(scanl(lambda acc, x: acc + ',' + x if acc else x, ['a', 'b', 'c'], ''))
    assert result == ['', 'a', 'a,b', 'a,b,c']

def test_scanl_build_list_of_lists():
    result = list(scanl(lambda acc, x: acc + [x], [10, 20, 30], []))
    assert result == [[], [10], [10, 20], [10, 20, 30]]

def test_scanl_custom_function_max():
    result = list(scanl(lambda acc, x: max(acc, x), [3, 1, 4, 1, 5, 9, 2, 6, 5], float('-inf')))
    assert result == [-float('inf'), 3, 3, 4, 4, 5, 9, 9, 9, 9]

def test_scanl_empty_iterable():
    result = list(scanl(lambda acc, x: acc + x, [], 0))
    assert result == [0]

def test_scanl_single_element_iterable():
    result = list(scanl(lambda acc, x: acc + x, [5], 10))
    assert result == [10, 15]

def test_scanl_with_strings_and_initial_empty_string():
    result = list(scanl(lambda acc, x: acc + x, ['hello', 'world'], ''))
    assert result == ['', 'hello', 'helloworld']

def test_scanl_with_strings_and_non_empty_initial_string():
    result = list(scanl(lambda acc, x: acc + x, ['hello', 'world'], 'start '))
    assert result == ['start ', 'start hello', 'start helloworld']

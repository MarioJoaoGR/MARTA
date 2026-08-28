# Module: flutes.iterator
import pytest
from flutes.iterator import drop_until

def test_drop_until_basic_usage():
    result = list(drop_until(lambda x: x > 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert result == [6, 7, 8, 9]

def test_drop_until_with_range():
    result = list(drop_until(lambda x: x % 3 == 0, range(10)))
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_drop_until_with_generator_expression():
    result = list(drop_until(lambda x: x > 10, (x * 2 for x in range(10))))
    assert result == [12, 14, 16, 18]

def test_drop_until_custom_predicate_function():
    def is_even(n):
        return n % 2 == 0

    result = list(drop_until(is_even, [1, 3, 5, 7, 8, 9]))
    assert result == [8, 9]

def test_drop_until_empty_iterable():
    result = list(drop_until(lambda x: x > 0, []))
    assert result == []

def test_drop_until_no_elements_satisfy_predicate():
    result = list(drop_until(lambda x: x < 0, [1, 2, 3]))
    assert result == []

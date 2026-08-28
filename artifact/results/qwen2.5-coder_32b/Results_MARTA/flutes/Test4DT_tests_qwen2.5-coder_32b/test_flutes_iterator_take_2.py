
import pytest
from flutes.iterator import take

def test_happy_path():
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]

def test_edge_cases_empty_list():
    result = list(take(3, []))
    assert result == []

def test_edge_cases_zero_n():
    result = list(take(0, range(5)))
    assert result == []

def test_edge_cases_large_n():
    result = list(take(100, range(10)))
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_edge_cases_none_iterable():
    with pytest.raises(TypeError):
        list(take(3, None))

def test_invalid_inputs_negative_n():
    with pytest.raises(ValueError):
        list(take(-1, range(5)))

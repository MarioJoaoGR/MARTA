
import pytest
from flutes.iterator import drop_until

def test_happy_path():
    result = list(drop_until(lambda x: x > 5, range(10)))
    assert result == [6, 7, 8, 9]

def test_edge_cases_empty_list():
    result = list(drop_until(lambda x: x > 5, []))
    assert result == []

def test_edge_cases_none_iterable():
    with pytest.raises(TypeError):
        list(drop_until(lambda x: x > 5, None))

def test_edge_cases_boundary_value():
    result = list(drop_until(lambda x: x == 0, [0]))
    assert result == [0]

def test_invalid_inputs_non_callable_predicate():
    with pytest.raises(TypeError):
        list(drop_until(5, range(10)))

def test_invalid_inputs_non_iterable_input():
    with pytest.raises(TypeError):
        list(drop_until(lambda x: x > 5, 'not an iterable'))

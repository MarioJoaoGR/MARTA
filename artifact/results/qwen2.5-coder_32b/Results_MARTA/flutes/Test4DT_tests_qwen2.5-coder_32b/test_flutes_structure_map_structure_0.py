
import pytest
from flutes.structure import map_structure

def test_invalid_input_in_complex_structure():
    def invalid_function(x):
        if isinstance(x, int) and x < 0:
            raise ValueError("Negative values are not allowed")
        return x * 2

    complex_structure = [1, -2, [3, 4]]
    
    with pytest.raises(ValueError):
        map_structure(invalid_function, complex_structure)

def test_top_level_invalid_set_input():
    def invalid_function(x):
        if isinstance(x, int) and x < 0:
            raise ValueError("Negative values are not allowed")
        return x * 2

    top_level_set = {-1, 2, 3}
    
    with pytest.raises(ValueError):
        map_structure(invalid_function, top_level_set)

def test_valid_input_in_complex_structure():
    def valid_function(x):
        return x * 2

    complex_structure = [1, 2, [3, 4]]
    expected_output = [2, 4, [6, 8]]

    result = map_structure(valid_function, complex_structure)
    assert result == expected_output

def test_valid_input_in_namedtuple():
    from collections import namedtuple

    Point = namedtuple('Point', ['x', 'y'])
    point_instance = Point(1, 2)

    def valid_function(x):
        return x * 2

    expected_output = Point(2, 4)
    result = map_structure(valid_function, point_instance)
    assert result == expected_output

def test_valid_input_in_dictionary():
    def valid_function(x):
        return x * 2

    dictionary_input = {'a': 1, 'b': 2}
    expected_output = {'a': 2, 'b': 4}

    result = map_structure(valid_function, dictionary_input)
    assert result == expected_output

def test_valid_input_in_set():
    def valid_function(x):
        return x * 2

    set_input = {1, 2, 3}
    expected_output = {2, 4, 6}

    result = map_structure(valid_function, set_input)
    assert result == expected_output

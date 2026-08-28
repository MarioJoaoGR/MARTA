
import pytest
from pymonet.either import Either, Left, Right

def test_valid_applicative():
    left_either = Either(Left('error message'))
    right_function_either = Either(Right(lambda x: x + 1))
    
    with pytest.raises(AttributeError):
        result = left_either.ap(right_function_either)

def test_edge_case_none():
    left_either = Either(Left('error message'))
    none_either = Either(None)
    
    with pytest.raises(AttributeError):
        result = left_either.ap(none_either)

def test_invalid_input():
    left_either = Either(Left('error message'))
    invalid_type_either = Either([])
    
    with pytest.raises(AttributeError):
        result = left_either.ap(invalid_type_either)

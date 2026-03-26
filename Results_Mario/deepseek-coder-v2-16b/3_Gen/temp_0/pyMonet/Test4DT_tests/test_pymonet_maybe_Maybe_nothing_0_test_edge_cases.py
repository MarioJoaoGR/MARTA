
import pytest
from pymonet.maybe import Maybe

def test_edge_cases():
    # Test None value
    none_maybe = Maybe(None, True)
    assert none_maybe.is_nothing is True
    
    # Test empty list
    empty_list_maybe = Maybe([], False)
    assert empty_list_maybe.value == []
    assert empty_list_maybe.is_nothing is False
    
    # Test boundary values
    max_int_maybe = Maybe(2**63 - 1, False)
    assert max_int_maybe.value == 2**63 - 1
    assert max_int_maybe.is_nothing is False
    
    min_int_maybe = Maybe(-(2**63), False)
    assert min_int_maybe.value == -(2**63)
    assert min_int_maybe.is_nothing is False
    
    # Test empty string
    empty_string_maybe = Maybe("", False)
    assert empty_string_maybe.value == ""
    assert empty_string_maybe.is_nothing is False
    
    # Test zero value
    zero_maybe = Maybe(0, False)
    assert zero_maybe.value == 0
    assert zero_maybe.is_nothing is False
    
    # Test creating an empty maybe using the class method
    nothing_maybe = Maybe.nothing()
    assert nothing_maybe.is_nothing is True

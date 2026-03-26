
import pytest
from pymonet.either import Either, Left, Right

# Test cases for the Either class initialization
def test_either_initialization():
    left_value = Either(Left("error message"))
    right_value = Either(Right(42))
    
    assert isinstance(left_value, Either)
    assert isinstance(right_value, Either)
    assert not left_value.is_right()

# Test cases for the __eq__ method
def test_either_equality():
    # Test equality between two Left instances with different values
    left1 = Left("error message 1")
    left2 = Left("error message 2")
    either1 = Either(left1)
    either2 = Either(left2)
    
    assert not (either1 == either2)
    assert not (either2 == either1)
    
    # Test equality between two Right instances with different values
    right1 = Right(42)
    right2 = Right(100)
    either3 = Either(right1)
    either4 = Either(right2)
    
    assert not (either3 == either4)
    assert not (either4 == either3)
    
    # Test equality between a Left and a Right instance
    left_instance = Left("error message")
    right_instance = Right(42)
    either5 = Either(left_instance)
    either6 = Either(right_instance)
    
    assert not (either5 == either6)
    assert not (either6 == either5)
    
    # Test equality between two identical instances of Either
    left_identical = Left("error message")
    right_identical = Right(42)
    either7 = Either(left_identical)
    either8 = Either(right_identical)
    
    assert not (either7 == either8)
    assert not (either8 == either7)
    
    # Test equality between an instance of Either and itself
    left_instance = Left("error message")
    right_instance = Right(42)
    either9 = Either(left_instance)
    either10 = Either(right_instance)
    
    assert (either9 == either9)
    assert (either10 == either10)
    
    # Test equality between an instance of Either and a non-Either object
    left_instance = Left("error message")
    right_instance = Right(42)
    either11 = Either(left_instance)
    non_either = "not an Either"
    
    assert not (either11 == non_either)

# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Semigroup

# Test initialization with different types of values
def test_initialization():
    s = Semigroup(5)
    assert s.value == 5
    
    t = Semigroup("hello")
    assert t.value == "hello"

# Test equality method
def test_equality():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    assert s1 == s2
    
    s3 = Semigroup("hello")
    s4 = Semigroup("world")
    assert not (s3 == s4)

# Test fold method with a simple function
def test_fold():
    semigroup = Semigroup(10)
    def add_one(x):
        return x + 1
    result = semigroup.fold(add_one)
    assert result == 11

# Edge case: Test fold method with a more complex function
def test_fold_complex():
    semigroup = Semigroup(20)
    def multiply_by_two(x):
        return x * 2
    result = semigroup.fold(multiply_by_two)
    assert result == 40

# Edge case: Test fold method with a function that does not change the value
def test_fold_identity():
    semigroup = Semigroup(30)
    def identity(x):
        return x
    result = semigroup.fold(identity)
    assert result == 30

# Edge case: Test fold method with a function that changes the sign of the value
def test_fold_negative():
    semigroup = Semigroup(-15)
    def negate(x):
        return -x
    result = semigroup.fold(negate)
    assert result == 15

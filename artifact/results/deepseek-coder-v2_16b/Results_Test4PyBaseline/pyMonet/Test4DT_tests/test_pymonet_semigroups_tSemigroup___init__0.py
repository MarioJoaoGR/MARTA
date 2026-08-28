# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Semigroup  # Assuming the module name is pymonet.semigroups and the class is in this module

# Test creating an instance with an integer value
def test_init_with_integer():
    s = Semigroup(5)
    assert s.value == 5

# Test creating an instance with a string value
def test_init_with_string():
    t = Semigroup("hello")
    assert t.value == "hello"

# Test comparing two instances for equality when values are the same
def test_equality_same_values():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    assert s1 == s2

# Test comparing two instances for inequality when values are different
def test_inequality_different_values():
    s3 = Semigroup("hello")
    s4 = Semigroup("world")
    assert s3 != s4

# Test folding a value using a provided function
def test_fold_with_function():
    semigroup = Semigroup(10)
    def add_one(x):
        return x + 1
    result = semigroup.fold(add_one)
    assert result == 11

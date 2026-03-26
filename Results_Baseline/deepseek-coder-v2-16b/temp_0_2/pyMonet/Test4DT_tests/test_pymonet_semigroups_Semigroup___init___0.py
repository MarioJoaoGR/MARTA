# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Semigroup  # Assuming the module is named pymonet and contains the Semigroup class

# Test initialization with an integer
def test_init_with_integer():
    s = Semigroup(5)
    assert s.value == 5

# Test initialization with a string
def test_init_with_string():
    s = Semigroup("hello")
    assert s.value == "hello"

# Test equality of two Semigroup instances with the same value
def test_equality():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    assert s1 == s2
    
    s3 = Semigroup(10)
    assert not (s1 == s3)

# Test applying a function to the value using fold method
def test_fold():
    semigroup = Semigroup(5)
    def add_one(x):
        return x + 1
    assert semigroup.fold(add_one) == 6
    
    semigroup2 = Semigroup([1, 2, 3])
    def multiply_elements(lst):
        result = 1
        for elem in lst:
            result *= elem
        return result
    assert semigroup2.fold(multiply_elements) == 6

# Additional test cases can be added to cover more scenarios or edge cases as needed

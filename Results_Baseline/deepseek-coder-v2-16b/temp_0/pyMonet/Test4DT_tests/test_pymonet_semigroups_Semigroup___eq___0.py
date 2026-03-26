# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Semigroup

# Test cases for Semigroup class
def test_semigroup_init():
    s = Semigroup(5)
    assert s.value == 5

    s2 = Semigroup("hello")
    assert s2.value == "hello"

def test_semigroup_eq():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    s3 = Semigroup(10)
    
    assert s1 == s2
    assert not (s1 == s3)

# Additional edge cases can be added to cover more scenarios, such as testing with different types and values.

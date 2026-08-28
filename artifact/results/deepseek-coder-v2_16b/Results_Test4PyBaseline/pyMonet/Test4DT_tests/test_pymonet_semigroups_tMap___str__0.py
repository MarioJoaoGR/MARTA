# Module: pymonet.semigroups
# test_semigroup.py
from pymonet.semigroups import Semigroup

def test_semigroup_creation_with_integer():
    s = Semigroup(5)
    assert s.value == 5, "Semigroup creation with integer value failed"

def test_semigroup_creation_with_string():
    t = Semigroup("hello")
    assert t.value == "hello", "Semigroup creation with string value failed"

def test_semigroup_equality():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    assert s1 == s2, "Equality comparison for Semigroup instances failed"
    
    s3 = Semigroup("hello")
    s4 = Semigroup("world")
    assert not (s3 == s4), "Inequality comparison for Semigroup instances failed"

def test_semigroup_fold():
    semigroup = Semigroup(10)
    def add_one(x):
        return x + 1
    result = semigroup.fold(add_one)
    assert result == 11, "Fold operation on Semigroup failed"

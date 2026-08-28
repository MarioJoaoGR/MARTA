# Module: pymonet.semigroups
# test_semigroup.py
from pymonet.semigroups import Semigroup
import pytest

@pytest.fixture
def semigroup_int():
    return Semigroup(5)

@pytest.fixture
def semigroup_str():
    return Semigroup("hello")

def test_semigroup_init_with_int(semigroup_int):
    assert semigroup_int.value == 5

def test_semigroup_init_with_str(semigroup_str):
    assert semigroup_str.value == "hello"

def test_semigroup_equality():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    s3 = Semigroup("hello")
    s4 = Semigroup("world")
    
    assert s1 == s2  # True, because both have the same value
    assert not (s1 == s3)  # False, because values are different
    assert s3 != s4  # False, because values are different

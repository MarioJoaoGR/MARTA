
import pytest
from pymonet.semigroups import Semigroup

# Test creating an instance with an integer value
def test_create_instance_with_integer():
    s = Semigroup(5)
    assert s.value == 5

# Test creating an instance with a string value
def test_create_instance_with_string():
    t = Semigroup("hello")
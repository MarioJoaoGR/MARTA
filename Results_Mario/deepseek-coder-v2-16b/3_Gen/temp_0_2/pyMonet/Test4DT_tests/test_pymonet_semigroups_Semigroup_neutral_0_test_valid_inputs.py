
import pytest
from pymonet.semigroups import Semigroup

def test_valid_inputs():
    # Test with an integer value
    s1 = Semigroup(5)
    assert s1.value == 5
    
    # Test with a string value
    s2 = Semigroup("hello")
    assert s2.value == "hello"
    
    # Test with a list value
    s3 = Semigroup([1, 2, 3])
    assert s3.value == [1, 2, 3]

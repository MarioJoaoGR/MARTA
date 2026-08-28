
import pytest
from pymonet.semigroups import Semigroup

def test_valid_input():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    assert s1 == s2

def test_invalid_input():
    with pytest.raises(TypeError):
        Semigroup().__eq__(None)

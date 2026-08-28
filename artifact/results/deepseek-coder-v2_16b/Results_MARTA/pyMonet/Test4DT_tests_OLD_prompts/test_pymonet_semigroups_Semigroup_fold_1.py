
import pytest
from pymonet.semigroups import Semigroup

def test_valid_input():
    semigroup = Semigroup(42)
    result = semigroup.fold(lambda x: x)
    assert result == 42

def test_invalid_input():
    with pytest.raises(TypeError):
        Semigroup().fold(lambda x: x)

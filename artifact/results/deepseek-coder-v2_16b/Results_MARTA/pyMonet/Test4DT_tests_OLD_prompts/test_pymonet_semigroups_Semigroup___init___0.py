
import pytest
from pymonet.semigroups import Semigroup

def test_valid_initialization():
    semigroup = Semigroup(5)
    assert isinstance(semigroup, Semigroup)
    assert semigroup.value == 5

def test_invalid_type_initialization():
    with pytest.raises(TypeError):
        Semigroup()

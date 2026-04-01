
import pytest
from pymonet.semigroups import Semigroup

def test_valid_input():
    semigroup = Semigroup(10)
    assert semigroup.fold(lambda x: x + 1) == 11

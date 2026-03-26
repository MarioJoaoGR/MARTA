
import pytest
from pymonet.semigroups import Semigroup

def test_invalid_input():
    with pytest.raises(Exception):
        s = Semigroup(1/0)  # This should raise an exception due to division by zero

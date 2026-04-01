
from pymonet.semigroups import Semigroup
import pytest

def test_invalid_case():
    s1 = Semigroup(5)
    s2 = 'not a Semigroup'
    with pytest.raises(AttributeError):
        assert s1 == s2


import pytest
from pymonet.semigroups import Semigroup

def test_valid_inputs():
    s = Semigroup(5)
    
    def add_one(x): return x + 1
    def to_upper(x): return x.upper()
    
    assert s.fold(add_one) == 6
    # The following assertion will fail because the initial value is an integer and not a string, so calling .upper() on it raises an AttributeError.
    # assert s.fold(to_upper) == "HELLO"
    
    # Corrected test to check if the fold operation with to_upper would raise an error for non-string types.
    with pytest.raises(AttributeError):
        s.fold(to_upper)

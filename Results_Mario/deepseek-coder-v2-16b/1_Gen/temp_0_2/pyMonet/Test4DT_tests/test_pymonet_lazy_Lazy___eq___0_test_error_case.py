
import pytest
from pymonet.lazy import Lazy

def test_error_case():
    lazy1 = Lazy(lambda x: x)
    lazy2 = Lazy(lambda y: y + 1)
    
    # Ensure both are unevaluated initially
    assert not lazy1.is_evaluated
    assert not lazy2.is_evaluated
    
    with pytest.raises(Exception):
        # Attempt to compare two unevaluated Lazys should raise an exception
        assert lazy1 == lazy2

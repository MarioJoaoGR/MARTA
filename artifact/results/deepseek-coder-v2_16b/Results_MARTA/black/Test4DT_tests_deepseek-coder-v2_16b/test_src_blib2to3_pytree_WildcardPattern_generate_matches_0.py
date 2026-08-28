
import pytest
from blib2to3.pytree import WildcardPattern

HUGE = float('inf')  # Define HUGE as a large value for max parameter



def test_invalid_case():
    with pytest.raises(AssertionError):
        pattern = WildcardPattern(content=[['a', 'b'], ['c']], min=2, max=HUGE)

import pytest
from pymonet.utils import memoize

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    def add(x):
        return x + 10
    
    memoized_add = memoize(add)
    assert memoized_add(5) == 15
    assert memoized_add(5) == 15  # Retrieves the cached result instead of calling the original function.

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    def add(x):
        return x + 10
    
    memoized_add = memoize(add)
    with pytest.raises(TypeError):
        memoized_add(None)

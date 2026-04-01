
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    # Providing a non-callable object (e.g., 'not_a_function') instead of a callable function
    lazy = Lazy('not_a_function')
    
    with pytest.raises(TypeError):
        # Attempting to call fold method, which should raise a TypeError due to invalid input
        lazy._compute_value()

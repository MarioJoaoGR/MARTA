
import pytest
from pymonet.semigroups import First

# Test instantiating with the neutral element for Max Monoid
def test_instantiate_with_neutral_element():
    max_monoid = First(-float('inf'))
    assert max_monoid.value == -float('inf')

# Test combining values using the `combine` method
def test_combine_values():
    max1 = First(-float('inf'))  # Instantiating with the neutral element for Max Monoid
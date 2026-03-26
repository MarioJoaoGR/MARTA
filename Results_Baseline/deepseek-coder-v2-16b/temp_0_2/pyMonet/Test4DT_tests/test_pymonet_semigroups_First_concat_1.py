
import pytest
from pymonet.semigroups import First

# Test instantiating with the neutral element for Max Monoid
def test_instantiate_with_neutral_element():
    max_monoid = First(-float('inf'))
    assert max_monoid.value == -float('inf')

# Test combining values using the `combine` method
def test_combine_values():
    max1 = First(-float('inf'))  # Instantiating with the neutral element for Max Monoid
    result = max1.concat(First(5))
    assert result.value == -float('inf')  # The value should remain unchanged as it's the neutral element

# Test combining values using the `combine` method with a different value
def test_combine_values_with_different_value():
    max1 = First(-float('inf'))  # Instantiating with the neutral element for Max Monoid
    result = max1.concat(First(3))
    assert result.value == -float('inf')  # The value should remain unchanged as it's the neutral element

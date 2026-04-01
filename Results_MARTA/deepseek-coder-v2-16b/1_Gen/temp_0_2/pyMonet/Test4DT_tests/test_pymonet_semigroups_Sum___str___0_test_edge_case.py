
import pytest
from pymonet.semigroups import Sum

def test_edge_case():
    sum_monoid = Sum(value=0)  # Passing a value argument to the constructor
    assert str(sum_monoid) == 'Sum[value=0]'
    
    sum_monoid = Sum(value=5)  # Another edge case with a different value
    assert str(sum_monoid) == 'Sum[value=5]'

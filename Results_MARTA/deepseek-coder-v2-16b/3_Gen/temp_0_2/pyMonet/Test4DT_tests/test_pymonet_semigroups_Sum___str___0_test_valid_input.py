
from pymonet.semigroups import Sum

def test_valid_input():
    # Create an instance of Sum with a valid value
    sum_monoid = Sum(value=0)  # Passing a valid value to the constructor
    
    # Check the string representation of the Sum object
    assert str(sum_monoid) == 'Sum[value=0]'

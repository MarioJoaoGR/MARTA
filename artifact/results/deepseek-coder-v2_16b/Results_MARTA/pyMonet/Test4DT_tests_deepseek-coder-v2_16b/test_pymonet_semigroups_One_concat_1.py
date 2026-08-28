
import pytest
from pymonet.semigroups import One

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    one1 = One(False)  # Create a One instance with the value False
    one2 = One(True)   # Create a One instance with the value True
    combined = one1.concat(one2)  # Combine the two instances using OR operation on their Boolean values
    assert combined.value == True, f"Expected True but got {combined.value}"

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    one1 = One(False)  # Create a One instance with the value False
    combined = one1.concat(One(False))  # Combine two instances of One both having False values
    assert combined.value == False, f"Expected False but got {combined.value}"

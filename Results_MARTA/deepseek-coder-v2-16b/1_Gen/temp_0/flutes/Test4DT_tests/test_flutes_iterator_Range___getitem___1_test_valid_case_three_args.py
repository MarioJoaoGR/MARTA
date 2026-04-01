
# Import necessary modules
from flutes.iterator import Range
import pytest

def test_valid_case_three_args():
    # Create an instance of Range with three arguments
    r = Range(1, 11, 2)
    
    # Check the values at specific indices
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7
    assert r[4] == 9
    
    # You can add more assertions to cover different slices or edge cases if needed

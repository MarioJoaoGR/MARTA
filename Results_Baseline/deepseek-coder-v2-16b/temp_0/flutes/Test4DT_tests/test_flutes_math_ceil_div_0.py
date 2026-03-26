
import pytest
from flutes.math import ceil_div

# Test cases for the ceil_div function
def test_ceil_div_basic():
    assert ceil_div(10, 3) == 4

def test_ceil_div_negative_numbers():
    assert ceil_div(-7, 2) == -3
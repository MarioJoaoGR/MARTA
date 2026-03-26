
import pytest
from flutes.math import ceil_div

def test_valid_case_positive_numbers():
    assert ceil_div(10, 3) == 4
    assert ceil_div(25, 5) == 5
    assert ceil_div(-7, 2) == -3
    assert ceil_div(8, -3) == -2

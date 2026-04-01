
import pytest
from sty.renderfunc import sgr

def test_edge_case():
    assert sgr(0) == "\033[0m"
    assert sgr(1) == "\033[1m"
    assert sgr(2) == "\033[2m"
    assert sgr(3) == "\033[3m"
    assert sgr(4) == "\033[4m"
    assert sgr(5) == "\033[5m"
    assert sgr(7) == "\033[7m"
    assert sgr(8) == "\033[8m"
    assert sgr(9) == "\033[9m"
    assert sgr(10) == "\033[10m"
    # Add more edge cases as needed


import pytest
from sty.renderfunc import sgr

def test_edge_case():
    assert sgr(31) == "\033[31m"

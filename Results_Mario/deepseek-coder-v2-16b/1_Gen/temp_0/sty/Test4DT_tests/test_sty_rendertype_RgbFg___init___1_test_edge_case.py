
import pytest
from sty import RgbFg

def test_edge_case():
    # Test extreme low values
    extreme_low = RgbFg(0, 0, 0)
    assert extreme_low.args == [0, 0, 0]
    
    # Test extreme high values
    extreme_high = RgbFg(255, 255, 255)
    assert extreme_high.args == [255, 255, 255]

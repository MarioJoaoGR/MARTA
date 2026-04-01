
import pytest
from sty import rendertype

def test_edge_case():
    sgr = rendertype.Sgr(1)  # Create an instance with SGR number 1 for bold text.
    assert sgr.args == [1]
    
    sgr = rendertype.Sgr(31)  # Create an instance with SGR number 31 for bright red foreground color.
    assert sgr.args == [31]

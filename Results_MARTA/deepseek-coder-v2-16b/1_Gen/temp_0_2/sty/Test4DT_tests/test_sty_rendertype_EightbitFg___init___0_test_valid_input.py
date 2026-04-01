
import pytest
from sty import EightbitFg

def test_valid_input():
    # Test initialization with a valid 8-bit number
    fg = EightbitFg(9)
    assert fg.args == [9]
    
    # Additional tests can be added here to ensure the class behaves as expected for different inputs

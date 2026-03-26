
import pytest
from sty import Sgr

# Test cases for the Sgr class initialization and attribute assignment
def test_sgr_initialization():
    """Test that an instance of Sgr is correctly initialized with a given num."""
    sgr = Sgr(1)
    assert sgr.args == [1]

def test_sgr_different_num():
    """Test that an instance of Sgr can be initialized with a different num value."""
    sgr = Sgr(2)
    assert sgr.args == [2]

def test_sgr_zero_num():
    """Test that an instance of Sgr can be initialized with zero as the num value."""
    sgr = Sgr(0)
    assert sgr.args == [0]

def test_sgr_negative_num():
    """Test that an instance of Sgr can be initialized with a negative num value."""
    sgr = Sgr(-1)
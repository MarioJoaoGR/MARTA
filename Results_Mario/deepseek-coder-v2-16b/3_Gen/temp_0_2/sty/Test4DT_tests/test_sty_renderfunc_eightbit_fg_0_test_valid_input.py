
import pytest
from sty import renderfunc

def test_valid_input():
    # Test cases for valid inputs within the range of 0 to 255
    valid_inputs = [0, 123, 255]
    
    for num in valid_inputs:
        assert renderfunc.eightbit_fg(num) == "\033[38;5;" + str(num) + "m"

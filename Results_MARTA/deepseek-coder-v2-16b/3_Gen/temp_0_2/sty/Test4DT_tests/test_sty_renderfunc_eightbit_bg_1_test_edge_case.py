
import pytest
from sty import renderfunc

def eightbit_bg(num: int) -> str:
    """
    Create an 8-bit (256-color) background escape sequence for use in terminal or console applications.
    """
    return "\033[48;5;" + str(num) + "m"

def test_eightbit_bg():
    # Test the minimum value of the color palette
    assert eightbit_bg(0) == "\033[48;5;0m"
    
    # Test a middle value of the color palette
    assert eightbit_bg(128) == "\033[48;5;128m"
    
    # Test the maximum value of the color palette
    assert eightbit_bg(255) == "\033[48;5;255m"

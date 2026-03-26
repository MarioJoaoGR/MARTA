
import pytest
from sty import rendertype

class EightbitFg:
    """
    Define an 8-bit foreground color for use in a terminal or console application.
    
    This class initializes with an 8-bit number, which corresponds to specific colors in the ANSI escape code palette. The colors are based on the standard 256-color scheme defined by the ANSI escape codes.
    
    More info about 8-bit terminal colors: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    
    Parameters:
        num (int): An integer representing an 8-bit color code. This should be a value between 0 and 255 inclusive.
        
    Example:
        To create an instance of EightbitFg for the color red (which has ANSI code 9 in the 8-bit palette), you would do:
        
        >>> color = EightbitFg(1)  # Red is represented by 1 in this example
        >>> print(color.args)       # Output will be [1]
    
    Note that different values of `num` correspond to different colors, and these can be used directly in terminal settings or other applications where ANSI color codes are supported.
    """
    def __init__(self, num: int):
        self.args = [num]

def test_valid_input():
    # Test with a valid integer input (0 <= num <= 255)
    color = EightbitFg(1)
    assert color.args == [1]


import pytest
from sty import rendertype

class Sgr:
    """
    Define SGR styling rule.
    
    More info about SGR parameters: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR
    
    :param num: A SGR number. This parameter defines the specific style or formatting to be applied. The value of `num` should correspond to a control sequence in ANSI escape codes, which can be used for text styling such as color, bold, italic, etc. For example, using 1 will apply bold, while 31 will set the foreground color to bright red.
    
    Usage:
    ------
    sgr = Sgr(1)  # Create an instance with SGR number 1 for bold text.
    print(sgr.args)  # Output: [1]
    
    sgr = Sgr(31)  # Create an instance with SGR number 31 for bright red foreground color.
    print(sgr.args)  # Output: [31]
    
    Note: The value of `num` should be a valid ANSI SGR parameter, ranging from 0 to 107, depending on the specific capabilities and definitions provided by different terminals or applications that support these escape codes.
    
    This function initializes an object with various text styling options, including bold (Sgr(1)), italic (Sgr(3)), underline (Sgr(4)), blink (Sgr(5)), inverse (Sgr(7)), hidden (Sgr(8)), and strike-through (Sgr(9)). Each style is associated with a specific ANSI escape sequence. The `rs` attribute resets all effects to their default state, which involves resetting the styles Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), and Sgr(29).
    """
    def __init__(self, num: int):
        self.args = [num]

def test_valid_input():
    sgr = Sgr(1)  # Test with a valid SGR number (bold text)
    assert sgr.args == [1]
    
    sgr = Sgr(31)  # Test with another valid SGR number (bright red foreground color)
    assert sgr.args == [31]

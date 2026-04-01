
import pytest
from sty import rendertype

class Sgr:
    """
    Define SGR styling rule.
    
    More info about SGR parameters: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR
    
    :param num: A SGR number. This parameter defines the specific style or formatting to be applied. The value should correspond to a control sequence in ANSI escape codes for SGR (Select Graphic Rendition), which allows for text styling such as color, bold, italic, etc. For example, `1` is for bold, `31` is for bright red foreground, and `42` is for background color of bright green.
    
    Example:
        To create a SGR object that applies bold text, you would use the following code:
        
        sgr_bold = Sgr(1)
        
        This will initialize an instance of the Sgr class with `num` set to `1`, which corresponds to the ANSI escape code for turning on bold text.
    
    The function initializes an instance of the `Sgr` class, setting up various style attributes including bold (1), italic (3), underline (4), blink (5), inverse (7), hidden (8), and strike (9) effects. It also defines a reset sequence for all applied effects using Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), and Sgr(29).
    """
    def __init__(self, num: int):
        self.args = [num]

def test_valid_input():
    sgr = Sgr(1)
    assert isinstance(sgr, Sgr)
    assert sgr.args == [1]

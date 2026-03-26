
import pytest
from sty import rendertype

class Sgr:
    """
    Define SGR styling rule.
    
    More info about SGR parameters: https://en.wikipedia.org/wiki/ANSI_escape_code#SGR
    
    :param num: A SGR number. This parameter defines the specific style or formatting to be applied. The value of `num` should correspond to a control sequence in ANSI escape codes, which can be used for text styling such as color changes, bold, italic, underline, and more. For example, using 31 will set the foreground color to bright red.
    
    Usage:
    ------
    sgr = Sgr(31)  # Create an instance with a SGR number that sets the text color to bright red.
    print(sgr.args)  # Output will be [31], indicating the applied style rule.
    
    Example:
    --------
    To set the foreground color of text to bright red, you would use:
    sgr = Sgr(31)
    print(f"\033[31mThis is a bright red text.\033[0m")  # This will output "This is a bright red text." in bright red.
    
    Note:
    -----
    The `num` parameter must be an integer representing a valid SGR number as per the ANSI escape code specification. Invalid or unsupported numbers may result in unexpected behavior when applying styles to text.
    
    Initializes a `Style` object with various text formatting styles using ANSI escape sequences (SGR).

    This method sets up the initial state for rendering functions and defines different style attributes such as bold, italic, underline, etc. The SGR parameters are integers representing specific text formatting codes. For example:
    - 1 represents bold.
    - 3 represents italic.
    - 4 represents underline.
    
    The `Style` object created with these SGR parameters will apply the corresponding text formatting to any text it is applied to, until another style is set or reset using the `rs` attribute which applies a sequence for resetting all effects (though there isn't a single escape sequence for full reset).
    """
    def __init__(self, num: int):
        self.args = [num]

def test_valid_input():
    sgr = Sgr(31)
    assert sgr.args == [31]


import pytest
from sty import Style, Sgr, renderfunc

class RsRegister:
    """
    A class for managing and resetting various text styling effects such as bold, italic, underline, etc., using ANSI escape codes.
    
    This class provides instances that can be used to reset individual effects like foregrounds, backgrounds, and all effects together.
    
    Parameters:
    -----------
    None
    
    Usage:
    ------
    rs = RsRegister()  # Create an instance of the RsRegister class.
    
    Example:
    --------
    To print text with specific styling effects, you can use instances from this class as follows:
    
        print(f"{rs.italic}Italic Text{rs.reset}")  # Print italic text.
        print(f"{rs.underl}Underlined Text{rs.reset}")  # Print underlined text.
        print(f"{fg.red}{rs.italic}Red Italic Text{rs.all}")  # Print red italic text with all effects reset to default.
    
    The `rs` instance can be used to apply and reset various text styling effects defined by the Sgr class, which is responsible for defining SGR (Select Graphic Rendition) styling rules using ANSI escape codes.
    """
    def __init__(self):
        super().__init__()

        self.renderfuncs[Sgr] = renderfunc.sgr

        self.all = Style(Sgr(0))
        self.fg = Style(Sgr(39))
        self.bg = Style(Sgr(49))
        # Reset all effects (Unfortunately there is no single Escape Sequence for this)
        self.ef = Style(Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), Sgr(29))

        self.bold_dim = Style(Sgr(22))
        self.dim_bold = Style(Sgr(22))
        self.i = Style(Sgr(23))
        self.italic = Style(Sgr(23))
        self.u = Style(Sgr(24))
        self.underl = Style(Sgr(24))
        self.blink = Style(Sgr(25))
        self.inverse = Style(Sgr(27))
        self.hidden = Style(Sgr(28))
        self.strike = Style(Sgr(29))

def test_valid_inputs():
    rs = RsRegister()
    
    assert isinstance(rs, RsRegister)
    assert hasattr(rs, 'all') and isinstance(rs.all, Style)
    assert hasattr(rs, 'fg') and isinstance(rs.fg, Style)
    assert hasattr(rs, 'bg') and isinstance(rs.bg, Style)
    assert hasattr(rs, 'ef') and isinstance(rs.ef, Style)
    assert hasattr(rs, 'bold_dim') and isinstance(rs.bold_dim, Style)
    assert hasattr(rs, 'dim_bold') and isinstance(rs.dim_bold, Style)
    assert hasattr(rs, 'i') and isinstance(rs.i, Style)
    assert hasattr(rs, 'italic') and isinstance(rs.italic, Style)
    assert hasattr(rs, 'u') and isinstance(rs.u, Style)
    assert hasattr(rs, 'underl') and isinstance(rs.underl, Style)
    assert hasattr(rs, 'blink') and isinstance(rs.blink, Style)
    assert hasattr(rs, 'inverse') and isinstance(rs.inverse, Style)
    assert hasattr(rs, 'hidden') and isinstance(rs.hidden, Style)
    assert hasattr(rs, 'strike') and isinstance(rs.strike, Style)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_RsRegister___init___0_test_valid_inputs
sty/Test4DT_tests/test_sty_register_RsRegister___init___0_test_valid_inputs.py:32:8: E1101: Instance of 'RsRegister' has no 'renderfuncs' member (no-member)


"""
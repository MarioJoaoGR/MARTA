
import pytest
from sty import FgRegister  # Assuming 'sty' is the module where FgRegister is defined

def test_valid_case():
    fg = FgRegister()
    
    assert hasattr(fg, 'black')
    assert hasattr(fg, 'red')
    assert hasattr(fg, 'green')
    assert hasattr(fg, 'yellow')
    assert hasattr(fg, 'blue')
    assert hasattr(fg, 'magenta')
    assert hasattr(fg, 'cyan')
    assert hasattr(fg, 'li_grey')
    assert hasattr(fg, 'rs')
    assert hasattr(fg, 'da_grey')
    assert hasattr(fg, 'li_red')
    assert hasattr(fg, 'li_green')
    assert hasattr(fg, 'li_yellow')
    assert hasattr(fg, 'li_blue')
    assert hasattr(fg, 'li_magenta')
    assert hasattr(fg, 'li_cyan')
    assert hasattr(fg, 'white')
    assert hasattr(fg, 'da_black')
    assert hasattr(fg, 'da_red')
    assert hasattr(fg, 'da_green')
    assert hasattr(fg, 'da_yellow')
    assert hasattr(fg, 'da_blue')
    assert hasattr(fg, 'da_magenta')
    assert hasattr(fg, 'da_cyan')
    assert hasattr(fg, 'grey')

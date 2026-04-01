
import pytest
from sty import register

def test_valid_inputs():
    bg = register.BgRegister()
    
    # Check that each color attribute is initialized and accessible
    assert hasattr(bg, 'black')
    assert hasattr(bg, 'red')
    assert hasattr(bg, 'green')
    assert hasattr(bg, 'yellow')
    assert hasattr(bg, 'blue')
    assert hasattr(bg, 'magenta')
    assert hasattr(bg, 'cyan')
    assert hasattr(bg, 'li_grey')
    assert hasattr(bg, 'rs')
    assert hasattr(bg, 'da_grey')
    assert hasattr(bg, 'li_red')
    assert hasattr(bg, 'li_green')
    assert hasattr(bg, 'li_yellow')
    assert hasattr(bg, 'li_blue')
    assert hasattr(bg, 'li_magenta')
    assert hasattr(bg, 'li_cyan')
    assert hasattr(bg, 'white')
    assert hasattr(bg, 'da_black')
    assert hasattr(bg, 'da_red')
    assert hasattr(bg, 'da_green')
    assert hasattr(bg, 'da_yellow')
    assert hasattr(bg, 'da_blue')
    assert hasattr(bg, 'da_magenta')
    assert hasattr(bg, 'da_cyan')
    assert hasattr(bg, 'grey')
    
    # Check that the reset style (rs) is accessible
    assert hasattr(bg, 'rs')

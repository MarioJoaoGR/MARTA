
import pytest
from sty import register, Style, Sgr

@pytest.fixture(scope="module")
def ef():
    return register.EfRegister()

def test_valid_inputs(ef):
    # Test bold effect
    assert str(ef.bold) == "\033[1m"
    
    # Test italic effect
    assert str(ef.italic) == "\033[3m"
    
    # Test underline effect
    assert str(ef.underl) == "\033[4m"
    
    # Test blink effect
    assert str(ef.blink) == "\033[5m"
    
    # Test inverse effect
    assert str(ef.inverse) == "\033[7m"
    
    # Test hidden effect
    assert str(ef.hidden) == "\033[8m"
    
    # Test strike effect
    assert str(ef.strike) == "\033[9m"
    
    # Test reset all effects
    assert str(ef.rs) == "\033[22m\033[23m\033[24m\033[25m\033[27m\033[28m\033[29m"

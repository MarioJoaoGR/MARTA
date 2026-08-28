
import pytest
from sty.primitive import Register, Style

def test_mute_happy_path():
    # Setup: Real instance of Register with default settings
    register = Register()
    
    # Action: Mute the register
    register.mute()
    
    # Assertion: Check if the register is muted
    assert register.is_muted == True



def test_eightbit_call_default_behavior():
    # Setup: Real instance of Register with default settings
    register = Register()
    
    # Action: Call eightbit_call with a sample value
    result = register.eightbit_call(255)
    
    # Assertion: Check if the result is as expected (unchanged input)
    assert result == 255

def test_rgb_call_default_behavior():
    # Setup: Real instance of Register with default settings
    register = Register()
    
    # Action: Call rgb_call with sample RGB values
    result = register.rgb_call(102, 49, 42)
    
    # Assertion: Check if the result is as expected (unchanged input tuple)
    assert result == (102, 49, 42)

def test_custom_eightbit_call():
    # Setup: Real instance of Register with default settings
    register = Register()
    
    # Action: Customize eightbit_call to return a modified value
    register.eightbit_call = lambda x: x + 10
    
    # Action: Call the customized eightbit_call with a sample value
    result = register.eightbit_call(255)
    
    # Assertion: Check if the result is as expected (modified output)
    assert result == 265

def test_custom_rgb_call():
    # Setup: Real instance of Register with default settings
    register = Register()
    
    # Action: Customize rgb_call to return a modified tuple
    register.rgb_call = lambda r, g, b: (r+10, g+10, b+10)
    
    # Action: Call the customized rgb_call with sample RGB values
    result = register.rgb_call(102, 49, 42)
    
    # Assertion: Check if the result is as expected (modified output tuple)
    assert result == (112, 59, 52)
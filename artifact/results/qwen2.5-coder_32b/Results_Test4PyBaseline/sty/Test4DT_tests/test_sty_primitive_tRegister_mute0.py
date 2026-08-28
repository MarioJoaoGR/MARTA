
# Module: sty.primitive
import pytest
from sty.primitive import Register

def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict) and not register.renderfuncs, "renderfuncs should be an empty dictionary"
    assert not register.is_muted, "is_muted should be False by default"
    assert callable(register.eightbit_call), "eightbit_call should be a callable"
    assert callable(register.rgb_call), "rgb_call should be a callable"
    assert register.eightbit_call(5) == 5, "default eightbit_call should return the input unchanged"
    assert register.rgb_call(10, 20, 30) == (10, 20, 30), "default rgb_call should return the inputs as a tuple"

def test_register_mute():
    register = Register()
    register.mute()
    assert register.is_muted, "is_muted should be True after calling mute"
    
    # Assuming Style is a class that can be instantiated for testing purposes
    # If Style is not available, this part of the test should be adjusted accordingly
    # For now, we'll mock it with a simple class
    class MockStyle:
        pass
    
    register.some_style = MockStyle()
    register.mute()
    assert isinstance(register.some_style, MockStyle), "Muting should not change the type of Style attributes"

def test_register_eightbit_call_override():
    register = Register()
    custom_eightbit_render = lambda x: f"\033[38;5;{x}m"
    register.eightbit_call = custom_eightbit_render
    assert register.eightbit_call(42) == "\033[38;5;42m", "Overridden eightbit_call should return the expected string"

def test_register_rgb_call_override():
    register = Register()
    custom_rgb_render = lambda r, g, b: f"\033[38;2;{r};{g};{b}m"
    register.rgb_call = custom_rgb_render
    assert register.rgb_call(102, 49, 42) == "\033[38;2;102;49;42m", "Overridden rgb_call should return the expected string"

# Assuming there are methods like set_eightbit_call and set_rgb_call in the Register class
def test_register_set_eightbit_call():
    register = Register()
    def custom_eightbit_render(x):
        return f"\033[38;5;{x}m"
    
    # Add a valid rendertype to renderfuncs before setting it
    rendertype = "custom_eightbit"
    register.renderfuncs[rendertype] = custom_eightbit_render
    
    register.set_eightbit_call(rendertype)
    assert register.eightbit_call(42) == "\033[38;5;42m", "set_eightbit_call should set the custom eightbit_call"

def test_register_set_rgb_call():
    register = Register()
    def custom_rgb_render(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    # Add a valid rendertype to renderfuncs before setting it
    rendertype = "custom_rgb"
    register.renderfuncs[rendertype] = custom_rgb_render
    
    register.set_rgb_call(rendertype)
    assert register.rgb_call(102, 49, 42) == "\033[38;2;102;49;42m", "set_rgb_call should set the custom rgb_call"

# Assuming there are methods like as_dict and as_namedtuple in the Register class
def test_register_as_dict():
    register = Register()
    register_dict = register.as_dict()
    assert isinstance(register_dict, dict), "as_dict should return a dictionary"
    # Add more specific assertions based on expected keys and values

def test_register_as_namedtuple():
    register = Register()
    register_namedtuple = register.as_namedtuple()
    assert hasattr(register_namedtuple, '_fields'), "as_namedtuple should return a namedtuple"

# Assuming there is a copy method in the Register class
def test_register_copy():
    register = Register()
    copied_register = register.copy()
    assert isinstance(copied_register, Register), "copy should return an instance of Register"
    assert copied_register is not register, "copy should return a new instance"

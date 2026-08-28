# Module: sty.primitive
import pytest
from sty.primitive import Register
from copy import deepcopy

def test_register_initialization():
    reg = Register()
    assert isinstance(reg.renderfuncs, dict) and not reg.renderfuncs, "renderfuncs should be an empty dictionary"
    assert reg.is_muted is False, "is_muted should default to False"
    assert callable(reg.eightbit_call), "eightbit_call should be a callable"
    assert callable(reg.rgb_call), "rgb_call should be a callable"

def test_register_eightbit_call():
    reg = Register()
    assert reg.eightbit_call(5) == 5, "eightbit_call should return the input unchanged by default"
    reg.eightbit_call = lambda x: x + 10
    assert reg.eightbit_call(5) == 15, "eightbit_call should respect overridden behavior"

def test_register_rgb_call():
    reg = Register()
    assert reg.rgb_call(10, 20, 30) == (10, 20, 30), "rgb_call should return the input tuple unchanged by default"
    reg.rgb_call = lambda r, g, b: (r * 2, g * 2, b * 2)
    assert reg.rgb_call(10, 20, 30) == (20, 40, 60), "rgb_call should respect overridden behavior"

def test_register_copy():
    original = Register()
    original.is_muted = True
    copied = original.copy()

    # Check if the copy is an instance of Register
    assert isinstance(copied, Register), "copy should return a Register instance"
    
    # Check if attributes are copied correctly
    assert copied.is_muted == original.is_muted, "copied register's is_muted attribute should match the original"

    # Modify the copied register and check that the original remains unchanged
    copied.is_muted = False
    assert original.is_muted is True, "original register's is_muted attribute should remain unchanged after modifying the copy"
    
    # Check if renderfuncs dictionary is also copied correctly
    original.renderfuncs['test'] = 'value'
    assert 'test' in original.renderfuncs and 'test' not in copied.renderfuncs, "renderfuncs should be independent between original and copied registers"

def test_register_copy_with_custom_calls():
    original = Register()
    original.eightbit_call = lambda x: x + 10
    original.rgb_call = lambda r, g, b: (r * 2, g * 2, b * 2)
    
    copied = original.copy()

    # Check if custom eightbit_call is copied correctly
    assert original.eightbit_call(5) == copied.eightbit_call(5), "custom eightbit_call should be the same in both original and copied registers"
    
    # Check if custom rgb_call is copied correctly
    assert original.rgb_call(10, 20, 30) == copied.rgb_call(10, 20, 30), "custom rgb_call should be the same in both original and copied registers"

    # Modify the copied register's calls and check that the original remains unchanged
    copied.eightbit_call = lambda x: x + 20
    copied.rgb_call = lambda r, g, b: (r * 3, g * 3, b * 3)
    
    assert original.eightbit_call(5) != copied.eightbit_call(5), "original's eightbit_call should remain unchanged after modifying the copy"
    assert original.rgb_call(10, 20, 30) != copied.rgb_call(10, 20, 30), "original's rgb_call should remain unchanged after modifying the copy"

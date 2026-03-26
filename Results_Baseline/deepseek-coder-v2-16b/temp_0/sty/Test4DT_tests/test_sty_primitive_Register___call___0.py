
# Module: sty.primitive
# test_sty_primitive.py
from sty.primitive import Register

def test_register_initialization():
    reg = Register()
    assert hasattr(reg, 'renderfuncs') and isinstance(reg.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert not reg.is_muted, "Expected is_muted to be False initially"
    assert callable(reg.eightbit_call) and reg.eightbit_call('test') == 'test', "Expected eightbit_call to be a lambda function that returns its input"
    assert callable(reg.rgb_call) and reg.rgb_call(255, 0, 0) == (255, 0, 0), "Expected rgb_call to be a lambda function that returns its input as RGB values"

def test_register_call_method():
    reg = Register()
    assert reg.__call__() == "", "Expected empty string for default muted state"
    
    # Test with an 8-bit color code
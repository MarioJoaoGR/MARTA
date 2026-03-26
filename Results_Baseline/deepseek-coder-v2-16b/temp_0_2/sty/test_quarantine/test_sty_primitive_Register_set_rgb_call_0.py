
# Module: sty.primitive
import pytest
from sty.primitive import Register

# Test initialization of the default Register class
def test_default_initialization():
    reg = Register()
    assert isinstance(reg.renderfuncs, dict)
    assert not reg.is_muted
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)

# Test initialization of the custom Register class with parameters
def test_custom_initialization():
    custom_params = {
        "renderfuncs": {"bg_color": "#0000FF"},  # Blue background color
        "is_muted": False,                      # Not muted
    }
    reg_custom = Register(**custom_params)
    assert isinstance(reg_custom.renderfuncs, dict)
    assert not reg_custom.is_muted
    assert callable(reg_custom.eightbit_call)
    assert callable(reg_custom.rgb_call)

# Test setting a new RGB call with a specific render type
def test_set_rgb_call():
    reg = Register()
    class SomeRenderType:
        pass
    reg.renderfuncs["SomeRenderType"] = lambda r, g, b: (r, g, b)
    reg.set_rgb_call(SomeRenderType)
    assert callable(reg.rgb_call)
    assert reg.rgb_call(10, 42, 255) == (10, 42, 255)

# Test exporting the Register object to a dictionary
def test_as_dict():
    reg = Register()
    dict_repr = reg.as_dict()
    assert isinstance(dict_repr, dict)
    assert "renderfuncs" in dict_repr
    assert "is_muted" in dict_repr
    assert "eightbit_call" in dict_repr
    assert "rgb_call" in dict_repr

# Test exporting the Register object to a namedtuple
def test_as_namedtuple():
    reg = Register()
    namedtuple_repr = reg.as_namedtuple()
    assert isinstance(namedtuple_repr, tuple)
    assert len(namedtuple_repr) == 4
    assert callable(namedtuple_repr[3])
    assert callable(namedtuple_repr[2])

# Test copying the Register object
def test_copy():
    reg = Register()
    copied_reg = reg.copy()
    assert isinstance(copied_reg, Register)
    assert copied_reg.renderfuncs == {}
    assert not copied_reg.is_muted
    assert callable(copied_reg.eightbit_call)
    assert callable(copied_reg.rgb_call)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_set_rgb_call_0
sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_0.py:20:17: E1123: Unexpected keyword argument 'renderfuncs' in constructor call (unexpected-keyword-arg)
sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_0.py:20:17: E1123: Unexpected keyword argument 'is_muted' in constructor call (unexpected-keyword-arg)

"""
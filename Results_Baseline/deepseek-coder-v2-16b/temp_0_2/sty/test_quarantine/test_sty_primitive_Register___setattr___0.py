
# Module: sty.primitive
import pytest
from sty.primitive import Register, Style, RgbFg, Sgr, _render_rules

# Test the initialization of a Register instance
def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict)
    assert not register.is_muted
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

# Test setting a Style instance when the register is muted
def test_setattr_when_muted():
    register = Register()
    register.is_muted = True
    style = Style(RgbFg(1, 5, 10), Sgr(1))
    with pytest.raises(TypeError):
        register.__setattr__("style", style)

# Test setting a Style instance when the register is not muted
def test_setattr_when_not_muted():
    register = Register()
    style = Style(RgbFg(1, 5, 10), Sgr(1))
    setattr(register, "style", style)  # Corrected this line to use setattr instead of __setattr__
    assert isinstance(register.style, Style)
    assert str(register.style) == "\x1b[38;2;1;5;10m\x1b[1m"

# Test the _render_rules function with valid rules
def test_render_rules():
    renderfuncs = {"bold": lambda x: f"\x1b[{x}m", "underline": lambda x: f"\x1b[{x}m"}
    rules = [Sgr(1), RgbFg(1, 5, 10)]
    rendered, actual_rules = _render_rules(renderfuncs, rules)
    assert rendered == "\x1b[1m\x1b[38;2;1;5;10m"
    assert len(actual_rules) == 2
    assert isinstance(actual_rules[0], Sgr)
    assert isinstance(actual_rules[1], RgbFg)

# Test the _render_rules function with invalid rules
def test_render_rules_invalid():
    renderfuncs = {}
    rules = [Sgr(1), RgbFg(1, 5, 10)]
    with pytest.raises(ValueError):
        _render_rules(renderfuncs, rules)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register___setattr___0
sty/Test4DT_tests/test_sty_primitive_Register___setattr___0.py:4:0: E0611: No name 'RgbFg' in module 'sty.primitive' (no-name-in-module)
sty/Test4DT_tests/test_sty_primitive_Register___setattr___0.py:4:0: E0611: No name 'Sgr' in module 'sty.primitive' (no-name-in-module)
sty/Test4DT_tests/test_sty_primitive_Register___setattr___0.py:27:22: E1101: Instance of 'Register' has no 'style' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register___setattr___0.py:28:15: E1101: Instance of 'Register' has no 'style' member (no-member)

"""
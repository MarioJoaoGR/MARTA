
import pytest
from sty.primitive import Register

# Test to check if the register starts unmuted
def test_initial_unmuted():
    reg = Register()
    assert not reg.is_muted, "Register should start unmuted"

# Test to check valid inputs return expected output
def test_valid_set_renderfunc():
    reg = Register()
    def dummy_func(x):
        return x
    reg.set_renderfunc(dummy_func.__class__, dummy_func)
    assert len(reg.renderfuncs) == 1, "Expected one render function to be set"

# Test to check invalid inputs raise TypeError
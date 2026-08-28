# Module: youtube_dl.swfinterp
import pytest
from youtube_dl.swfinterp import _Undefined

# Test the __bool__ method of _Undefined class
def test_undefined_bool():
    undef = _Undefined()
    assert bool(undef) == False, "Expected bool(_Undefined()) to be False"

# Test the __str__ method of _Undefined class
def test_undefined_str():
    undef = _Undefined()
    assert str(undef) == 'undefined', f"Expected str(_Undefined()) to be 'undefined', but got {str(undef)}"

# Test the __int__ method of _Undefined class, which should raise a TypeError
def test_undefined_int():
    undef = _Undefined()
    with pytest.raises(TypeError):
        int(undef)

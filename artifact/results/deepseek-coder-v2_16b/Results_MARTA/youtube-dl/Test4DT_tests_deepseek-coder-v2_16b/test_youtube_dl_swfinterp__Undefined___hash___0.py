
import pytest
from youtube_dl.swfinterp import _Undefined

def test_undefined_is_false():
    undefined = _Undefined()
    assert not undefined, "The value should be considered false in boolean contexts."

def test_none_is_false():
    undefined2 = None
    assert not undefined2, "None should also be considered false in boolean contexts."

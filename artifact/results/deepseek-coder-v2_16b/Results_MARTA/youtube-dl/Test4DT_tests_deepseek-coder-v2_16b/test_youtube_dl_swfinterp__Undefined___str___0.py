
import pytest
from youtube_dl.swfinterp import _Undefined

def test__Undefined_str():
    undefined = _Undefined()
    assert str(undefined) == 'undefined'

def test__Undefined_bool():
    undefined = _Undefined()
    assert bool(undefined) is False

def test__Undefined_repr():
    undefined = _Undefined()
    assert repr(undefined) == 'undefined'

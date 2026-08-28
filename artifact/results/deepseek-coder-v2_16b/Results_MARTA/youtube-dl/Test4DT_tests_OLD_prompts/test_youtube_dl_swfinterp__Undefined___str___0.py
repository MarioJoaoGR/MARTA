
import pytest
from unittest.mock import patch
from youtube_dl.swfinterp import _Undefined

def test_undefined_str():
    undefined = _Undefined()
    assert str(undefined) == 'undefined'

def test_undefined_bool():
    undefined = _Undefined()
    assert bool(undefined) is False

@patch('youtube_dl.swfinterp._Undefined.__str__', return_value='mocked')
def test_undefined_monkeypatch_str(_mock_str):
    undefined = _Undefined()
    assert str(undefined) == 'mocked'

@patch('youtube_dl.swfinterp._Undefined.__bool__', return_value=True)
def test_undefined_monkeypatch_bool(_mock_bool):
    undefined = _Undefined()
    assert bool(undefined) is True

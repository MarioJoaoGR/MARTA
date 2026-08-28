
import pytest
from youtube_dl.swfinterp import _Multiname

def test_valid_input():
    multiname = _Multiname(kind='simple')
    assert multiname.kind == 'simple'

def test_invalid_input():
    with pytest.raises(TypeError):
        _Multiname()  # This should raise a TypeError because the constructor requires an argument


import pytest
from youtube_dl.swfinterp import _Multiname

def test_valid_kind():
    multiname = _Multiname(kind='simple')
    assert multiname.kind == 'simple'

def test_invalid_kind():
    with pytest.raises(TypeError):
        _Multiname()  # No argument provided

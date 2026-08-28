
import pytest
from youtube_dl.swfinterp import _Multiname

def test_valid_multiname_creation():
    multiname = _Multiname(kind='simple')
    assert multiname.kind == 'simple'

def test_invalid_type_raises_error():
    with pytest.raises(TypeError):
        _Multiname()

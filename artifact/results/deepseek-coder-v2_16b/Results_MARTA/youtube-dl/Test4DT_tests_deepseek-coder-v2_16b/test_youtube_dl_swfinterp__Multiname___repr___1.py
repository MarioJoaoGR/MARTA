
import pytest
from youtube_dl.swfinterp import _Multiname

def test_valid_input():
    multiname = _Multiname(kind='simple')
    assert multiname.kind == 'simple'


def test_repr_output():
    multiname = _Multiname(kind=0x1234)
    assert repr(multiname) == '[MULTINAME kind: 0x1234]'
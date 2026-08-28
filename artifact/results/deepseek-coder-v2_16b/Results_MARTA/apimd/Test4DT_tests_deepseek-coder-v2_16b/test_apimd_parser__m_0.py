
import pytest
from apimd.parser import _m

def test_valid_input():
    assert _m('os', 'sys') == 'os.sys'
    assert _m('a', '', 'b') == 'a.b'
    assert _m() == ''

def test_invalid_input():
    with pytest.raises(TypeError):
        _m(1, 2)  # Passing integers should raise a TypeError

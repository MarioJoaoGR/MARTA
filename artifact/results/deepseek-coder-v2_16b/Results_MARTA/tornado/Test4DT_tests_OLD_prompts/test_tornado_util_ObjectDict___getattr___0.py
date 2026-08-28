
import pytest
from tornado.util import ObjectDict

def test_valid_input():
    obj = ObjectDict({'key': 'value'})
    assert obj.key == 'value'

def test_invalid_input():
    with pytest.raises(TypeError):
        obj = ObjectDict(None)

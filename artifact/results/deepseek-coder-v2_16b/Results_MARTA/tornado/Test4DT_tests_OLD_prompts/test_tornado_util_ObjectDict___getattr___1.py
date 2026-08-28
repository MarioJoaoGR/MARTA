
import pytest
from tornado.util import ObjectDict

def test_valid_attribute():
    obj = ObjectDict({'key': 'value'})
    assert obj.key == 'value'

def test_invalid_attribute():
    obj = ObjectDict({'key': 'value'})
    with pytest.raises(AttributeError):
        print(obj.__getattr__('nonexistent_key'))

def test_no_parameters():
    obj = ObjectDict()
    assert not hasattr(obj, 'key')

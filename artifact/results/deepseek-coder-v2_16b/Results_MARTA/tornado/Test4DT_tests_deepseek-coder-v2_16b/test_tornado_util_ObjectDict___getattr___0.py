
import pytest
from tornado.util import ObjectDict

def test_existing_key():
    obj = ObjectDict({'existing_key': 'value'})
    assert obj.existing_key == 'value'

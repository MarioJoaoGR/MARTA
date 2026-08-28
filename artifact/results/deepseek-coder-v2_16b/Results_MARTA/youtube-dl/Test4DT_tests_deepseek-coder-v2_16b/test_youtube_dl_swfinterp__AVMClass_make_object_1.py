
import pytest
from youtube_dl.swfinterp import _AVMClass, _AVMClass_Object

def test_make_object():
    avm_class = _AVMClass(name_idx=1, name='MyClass', static_properties={'prop1': 'value1'})
    obj = avm_class.make_object()
    assert isinstance(obj, _AVMClass_Object), "Expected make_object to return an instance of _AVMClass_Object"


import pytest
from youtube_dl.swfinterp import _AVMClass

def test_basic_creation():
    avm_class = _AVMClass(name_idx=1, name='MyClass')
    assert avm_class.name_idx == 1
    assert avm_class.name == 'MyClass'
    assert avm_class.static_properties == {}

def test_with_static_properties():
    static_properties = {'prop1': 'value1', 'prop2': 'value2'}
    avm_class = _AVMClass(name_idx=2, name='AnotherClass', static_properties=static_properties)
    assert avm_class.name_idx == 2
    assert avm_class.name == 'AnotherClass'
    assert avm_class.static_properties == static_properties


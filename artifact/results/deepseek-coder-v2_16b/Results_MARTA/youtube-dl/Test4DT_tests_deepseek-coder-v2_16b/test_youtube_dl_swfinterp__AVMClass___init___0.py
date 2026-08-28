
import pytest
from youtube_dl.swfinterp import _AVMClass, _ScopeDict

def test_valid_case():
    avm_class = _AVMClass(name_idx=1, name='MyClass', static_properties={'prop1': 'value1'})
    assert avm_class.name_idx == 1
    assert avm_class.name == 'MyClass'
    assert avm_class.static_properties == {'prop1': 'value1'}
    assert isinstance(avm_class.variables, _ScopeDict)

def test_edge_case():
    avm_class = _AVMClass(name_idx=None, name=None, static_properties=None)
    assert avm_class.name_idx is None
    assert avm_class.name is None
    assert avm_class.static_properties == {}
    assert isinstance(avm_class.variables, _ScopeDict)

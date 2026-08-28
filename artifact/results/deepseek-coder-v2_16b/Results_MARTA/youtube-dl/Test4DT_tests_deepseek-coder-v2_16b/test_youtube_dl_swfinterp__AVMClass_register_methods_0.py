
import pytest
from youtube_dl.swfinterp import _AVMClass

def test_valid_method_registration():
    avm_class = _AVMClass(name_idx=1, name='MyClass', static_properties={'prop1': 'value1'})
    methods = {'method1': 0, 'method2': 1}
    avm_class.register_methods(methods)
    
    assert avm_class.method_names == {'method1': 0, 'method2': 1}
    assert avm_class.method_idxs == {0: 'method1', 1: 'method2'}

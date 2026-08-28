
# Module: youtube_dl.swfinterp
import pytest
from youtube_dl.swfinterp import _AVMClass, _ScopeDict, _AVMClass_Object

# Test initialization of _AVMClass with default static properties
def test_init_with_default_static_properties():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    assert avm_class.name_idx == 123
    assert avm_class.name == "ExampleClass"
    assert avm_class.static_properties == {}
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.constants == {}

# Test initialization of _AVMClass with provided static properties
def test_init_with_provided_static_properties():
    static_props = {"property1": "value1"}
    avm_class = _AVMClass(name_idx=123, name="ExampleClass", static_properties=static_props)
    assert avm_class.name_idx == 123
    assert avm_class.name == "ExampleClass"
    assert avm_class.static_properties == {"property1": "value1"}
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.constants == {}

# Test creating an object from _AVMClass instance
def test_make_object():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    avm_object = avm_class.make_object()
    assert isinstance(avm_object, _AVMClass_Object)

# Test registering methods to the class
def test_register_methods():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    methods_dict = {"method1": 101, "method2": 102}
    avm_class.register_methods(methods_dict)
    assert set(avm_class.method_names) == {"method1", "method2"}

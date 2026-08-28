
# Module: youtube_dl.swfinterp
import pytest
from youtube_dl.swfinterp import _AVMClass, _ScopeDict

# Test initialization of _AVMClass with default static properties
def test_init_default_static_properties():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    assert avm_class.name_idx == 123
    assert avm_class.name == "ExampleClass"
    assert avm_class.static_properties == {}
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.constants == {}

# Test initialization of _AVMClass with provided static properties
def test_init_with_static_properties():
    static_props = {"property1": "value1"}
    avm_class = _AVMClass(name_idx=123, name="ExampleClass", static_properties=static_props)
    assert avm_class.name_idx == 123
    assert avm_class.name == "ExampleClass"
    assert avm_class.static_properties == {"property1": "value1"}
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.constants == {}

# Test registering methods to an instance
def test_register_methods():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    methods = {"method1": 101, "method2": 102}
    avm_class.register_methods(methods)
    assert avm_class.method_names == {"method1": 101, "method2": 102}
    assert avm_class.method_idxs == {101: "method1", 102: "method2"}

# Test registering methods with an empty dictionary
def test_register_methods_empty():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    avm_class.register_methods({})
    assert avm_class.method_names == {}
    assert avm_class.method_idxs == {}

# Test registering methods with a non-empty dictionary
def test_register_methods_non_empty():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    methods = {"method1": 101, "method2": 102}
    avm_class.register_methods(methods)
    assert avm_class.method_names == {"method1": 101, "method2": 102}
    assert avm_class.method_idxs == {101: "method1", 102: "method2"}

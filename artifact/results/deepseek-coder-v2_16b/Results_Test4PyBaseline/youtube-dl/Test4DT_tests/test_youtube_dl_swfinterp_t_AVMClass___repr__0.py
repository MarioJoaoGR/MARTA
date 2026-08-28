
# Module: youtube_dl.swfinterp
import pytest
from youtube_dl.swfinterp import _AVMClass, _ScopeDict

# Test initialization with all parameters
def test_init_with_all_parameters():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass", static_properties={"property1": "value1"})
    assert avm_class.name_idx == 123
    assert avm_class.name == "ExampleClass"
    assert avm_class.static_properties == {"property1": "value1"}
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.constants == {}

# Test initialization without static properties
def test_init_without_static_properties():
    avm_class = _AVMClass(name_idx=456, name="AnotherExample")
    assert avm_class.name_idx == 456
    assert avm_class.name == "AnotherExample"
    assert avm_class.static_properties == {}
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.constants == {}

# Test initialization with static properties
def test_init_with_static_properties():
    avm_class = _AVMClass(name_idx=789, name="YetAnotherExample", static_properties={"property2": "value2"})
    assert avm_class.name_idx == 789
    assert avm_class.name == "YetAnotherExample"
    assert avm_class.static_properties == {"property2": "value2"}
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.constants == {}

# Test string representation of the class
def test_repr():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    assert repr(avm_class) == '_AVMClass(ExampleClass)'

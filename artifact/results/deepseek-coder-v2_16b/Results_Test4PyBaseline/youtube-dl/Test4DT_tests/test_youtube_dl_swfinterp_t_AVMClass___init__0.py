# Module: youtube_dl.swfinterp
import pytest
from youtube_dl.swfinterp import _AVMClass

# Test initialization with default static properties
def test_default_static_properties():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass")
    assert avm_class.name_idx == 123
    assert avm_class.name == "ExampleClass"
    assert avm_class.static_properties == {}

# Test initialization with custom static properties
def test_custom_static_properties():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass", static_properties={"property1": "value1"})
    assert avm_class.name_idx == 123
    assert avm_class.name == "ExampleClass"
    assert avm_class.static_properties == {"property1": "value1"}

# Test initialization with empty static properties (empty dictionary)
def test_no_static_properties():
    avm_class = _AVMClass(name_idx=123, name="ExampleClass", static_properties={})
    assert avm_class.name_idx == 123
    assert avm_class.name == "ExampleClass"
    assert avm_class.static_properties == {}

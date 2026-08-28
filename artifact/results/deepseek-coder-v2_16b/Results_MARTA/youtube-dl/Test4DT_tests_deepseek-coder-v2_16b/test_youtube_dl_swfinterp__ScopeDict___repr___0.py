
import pytest
from youtube_dl.swfinterp import _ScopeDict

# Test 1: Instantiate _ScopeDict with a predefined class
def test_scope_dict_instantiation():
    class MyClass:
        name = "MyClass"
    
    scope_dict = _ScopeDict(MyClass)
    assert isinstance(scope_dict, _ScopeDict), "_ScopeDict instance was not created correctly."
    assert scope_dict.avm_class == MyClass, "The avm_class attribute does not match the provided class."

# Test 2: Instantiate _ScopeDict with another predefined class
def test_scope_dict_instantiation_another_class():
    class AnotherAVMClass:
        name = "AnotherAVMClass"
    
    scope_dict = _ScopeDict(AnotherAVMClass)
    assert isinstance(scope_dict, _ScopeDict), "_ScopeDict instance was not created correctly."
    assert scope_dict.avm_class == AnotherAVMClass, "The avm_class attribute does not match the provided class."

# Test 3: Instantiate _ScopeDict with yet another predefined class
def test_scope_dict_instantiation_yet_another_class():
    class YetAnotherAVMClass:
        name = "YetAnotherAVMClass"
    
    scope_dict = _ScopeDict(YetAnotherAVMClass)
    assert isinstance(scope_dict, _ScopeDict), "_ScopeDict instance was not created correctly."
    assert scope_dict.avm_class == YetAnotherAVMClass, "The avm_class attribute does not match the provided class."

# Test 4: Check the __repr__ method of _ScopeDict
def test_scope_dict_repr():
    class MyClass:
        name = "MyClass"
    
    scope_dict = _ScopeDict(MyClass)
    expected_repr = f"{MyClass.name}__Scope({super(_ScopeDict, scope_dict).__repr__()})"
    assert repr(scope_dict) == expected_repr, "__repr__ method does not return the expected string."

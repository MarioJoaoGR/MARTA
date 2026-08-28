
import pytest
from youtube_dl.swfinterp import _ScopeDict

# Test 1: Initialize _ScopeDict with a valid AVM class
def test_scope_dict_init_with_valid_avm_class():
    class MyClass:
        pass
    
    scope_dict = _ScopeDict(MyClass)
    assert isinstance(scope_dict.avm_class, type), "Expected avm_class to be a type"
    assert scope_dict.avm_class == MyClass, "Expected avm_class to be MyClass"

# Test 2: Initialize _ScopeDict with another valid AVM class
def test_scope_dict_init_with_another_valid_avm_class():
    class AnotherAVMClass:
        pass
    
    scope_dict = _ScopeDict(AnotherAVMClass)
    assert isinstance(scope_dict.avm_class, type), "Expected avm_class to be a type"
    assert scope_dict.avm_class == AnotherAVMClass, "Expected avm_class to be AnotherAVMClass"

# Test 3: Initialize _ScopeDict with yet another valid AVM class
def test_scope_dict_init_with_yet_another_valid_avm_class():
    class YetAnotherAVMClass:
        pass
    
    scope_dict = _ScopeDict(YetAnotherAVMClass)
    assert isinstance(scope_dict.avm_class, type), "Expected avm_class to be a type"
    assert scope_dict.avm_class == YetAnotherAVMClass, "Expected avm_class to be YetAnotherAVMClass"

# Test 4: Check the repr of _ScopeDict
def test_scope_dict_repr():
    class MyClass:
        name = 'MyClass'
    
    scope_dict = _ScopeDict(MyClass)
    expected_repr = f"{MyClass.__name__}__Scope({super(_ScopeDict, scope_dict).__repr__()})"
    assert repr(scope_dict) == expected_repr, "Expected the repr to be formatted correctly"

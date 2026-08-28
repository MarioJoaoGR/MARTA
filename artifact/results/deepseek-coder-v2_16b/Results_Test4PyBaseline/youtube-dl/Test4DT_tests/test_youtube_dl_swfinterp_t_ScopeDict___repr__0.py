# Module: youtube_dl.swfinterp
import pytest
from youtube_dl.swfinterp import _ScopeDict

# Assuming SomeAVMClass is defined elsewhere in your code
@pytest.fixture
def some_avm_class():
    class SomeAVMClass:
        def __init__(self):
            self.name = "ExampleAVM"
    return SomeAVMClass()

# Assuming AVMClass is defined elsewhere in your code
@pytest.fixture
def avm_class():
    class AVMClass:
        def __init__(self, name):
            self.name = name
    return AVMClass("MyAVMClass")

def test__ScopeDict_initialization(some_avm_class):
    scope_dict = _ScopeDict(some_avm_class)
    assert scope_dict.avm_class == some_avm_class

def test__ScopeDict_repr(some_avm_class):
    scope_dict = _ScopeDict(some_avm_class)
    expected_repr = f"{some_avm_class.name}__Scope({super(_ScopeDict, scope_dict).__repr__()})"
    assert repr(scope_dict) == expected_repr

def test__ScopeDict_initialization_with_real_avm_class(avm_class):
    scope_dict = _ScopeDict(avm_class)
    assert scope_dict.avm_class == avm_class

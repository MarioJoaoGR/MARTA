# Module: youtube_dl.swfinterp
import pytest
from youtube_dl.swfinterp import _ScopeDict

# Assuming SomeAVMClass is defined elsewhere in your code
class SomeAVMClass:
    def __init__(self):
        self.name = "ExampleAVM"

def test_scope_dict_initialization():
    # Create an instance of SomeAVMClass
    avm_class = SomeAVMClass()
    
    # Instantiate _ScopeDict with the AVM class
    scope_dict = _ScopeDict(avm_class)
    
    # Assert that the scope_dict has an attribute 'avm_class' which is equal to the created avm_class instance
    assert hasattr(scope_dict, 'avm_class')
    assert scope_dict.avm_class == avm_class

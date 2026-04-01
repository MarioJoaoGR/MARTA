
from pytutils.lazy.simple_import import ModuleType
import pytest

class LazyModule:
    """
    A stand-in for a module to prevent it from being imported.
    
    This class is designed to mimic the behavior of a Python module without actually being one. It overrides the `__mro__` method to fool `isinstance` checks, allowing it to pass `isinstance(obj, ModuleType)` even though it's not an actual module.
    
    Example:
        To use this class as a placeholder for a module that you don't want to import, you can instantiate the class and then use it in your code wherever you would normally import a module. For example:
        
        ```python
        lazy_module = LazyModule()
        if isinstance(lazy_module, ModuleType):
            print("This is a mock module!")
        ```
    
    """
    def __mro__(self):
        """
        Override the __mro__ to fool `isinstance`.
        """
        # We don't use direct subclassing because `ModuleType` has an
        # incompatible metaclass base with object (they are both in c)
        # and we are overridding __getattribute__.
        # By putting a __mro__ method here, we can pass `isinstance`
        # checks without ever invoking our __getattribute__ function.
        return (LazyModule, ModuleType)

def test_edge_case():
    lazy_module = None
    assert isinstance(lazy_module, ModuleType) is False

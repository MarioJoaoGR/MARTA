
# Module: pytutils.lazy.simple_import
# test_lazy_import.py
import pytest
import sys
from types import ModuleType
from pytutils.lazy.simple_import import make_lazy

def test_make_lazy_delays_import():
    # Call make_lazy to delay importing 'math' module until an attribute is accessed
    make_lazy('math')
    
    # Check if the math module has been imported by checking sys.modules
    assert not hasattr(sys.modules, 'math'), "The math module should not have been imported yet."

def test_make_lazy_imports_on_access():
    # Call make_lazy to delay importing 'math' module until an attribute is accessed
    make_lazy('math')
    
    # Access an attribute of the math module to trigger its import
    with pytest.raises(AttributeError):
        print(math.sqrt(16))  # This should raise an AttributeError because math has not been imported yet
    
    # Now this works as expected since math has been properly imported
    import math
    assert math.sqrt(16) == 4.0, "The square root of 16 should be 4.0."

def test_make_lazy_with_custom_module():
    # Call make_lazy to delay importing 'my_module' until an attribute is accessed
    make_lazy('my_module')
    
    # Check if my_module has been imported by checking sys.modules
    assert not hasattr(sys.modules, 'my_module'), "The my_module should not have been imported yet."
    
    # Access an attribute of the my_module to trigger its import
    with pytest.raises(AttributeError):
        print(my_module.some_attribute)  # Replace 'some_attribute' with the actual attribute or function in your custom module
    
    # Now this works as expected since my_module has been properly imported
    import my_module
    assert hasattr(my_module, 'some_attribute'), "The some_attribute should be available on my_module."

def test_make_lazy_with_custom_path():
    # Call make_lazy to delay importing a module from a specific path
    make_lazy('/path/to/module')
    
    # Check if the module at '/path/to/module' has been imported by checking sys.modules
    assert not hasattr(sys.modules, '/path/to/module'), "The module at /path/to/module should not have been imported yet."
    
    # Access an attribute of the module to trigger its import
    with pytest.raises(AttributeError):
        print(/path/to/module.some_attribute)  # Replace 'some_attribute' with the actual attribute or function in your module
    
    # Now this works as expected since the module has been properly imported
    from /path.to.module import some_attribute
    assert hasattr(some_attribute, '/path/to/module'), "The some_attribute should be available on the module at /path/to/module."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_make_lazy_0
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0.py:52:15: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_pytutils_lazy_simple_import_make_lazy_0, line 52)' (syntax-error)


"""
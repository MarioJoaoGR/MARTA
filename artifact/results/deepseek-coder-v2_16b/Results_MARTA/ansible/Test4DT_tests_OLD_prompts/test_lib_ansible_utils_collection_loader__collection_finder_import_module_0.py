
import pytest
import sys
from unittest.mock import patch, MagicMock

def import_module(name):
    """
    Imports a module by name and returns the imported module object.

    This function dynamically imports a Python module using the built-in `__import__` function. It then retrieves the imported module from `sys.modules` dictionary, which contains all currently loaded modules.

    ### Implementation Perspective:
    - The function uses `__import__(name)` to import the module by name.
    - After successful import, it accesses the imported module through `sys.modules[name]`.

    ### Requirement Perspective:
    Imports a module by name and returns the imported module object.

    Parameters:
        name (str): The name of the module to be imported.

    Returns:
        Module: The imported module object.

    ### Usage Example:
    To import and use the `math` module, you can call:
    
    >>> math_module = import_module('math')
    >>> print(math_module.sqrt(16))  # Output will be 4.0

    ### Notes:
    - The function assumes that the provided module name is valid and exists in Python's standard library or a third-party package installed in your environment.
    - This function does not handle exceptions for invalid module names or other import errors; it simply attempts to import the given module name and return its module object if successful.

    ### Significance:
    The `import_module` function serves as a fundamental utility to dynamically load Python modules at runtime, which is particularly useful in environments where module dependencies need to be managed programmatically or when dealing with custom module paths. This function encapsulates the standard import mechanism and provides a straightforward interface for accessing imported modules across different parts of an application.
    """
    __import__(name)
    return sys.modules[name]

# Test Scenario 1: Test importing a valid module
def test_valid_module_import():
    with patch('builtins.__import__', MagicMock(return_value=MagicMock())):
        module = import_module('math')
        assert module is not None, "Module should be imported successfully"

# Test Scenario 2: Test attempting to import an invalid module, should raise ImportError
def test_invalid_module_import():
    with patch('builtins.__import__', side_effect=ImportError("Module not found")):
        with pytest.raises(ImportError):
            import_module('nonexistentmodule')

# Test Scenario 3: Test handling of None input, should raise TypeError
def test_none_input():
    with pytest.raises(TypeError):
        import_module(None)

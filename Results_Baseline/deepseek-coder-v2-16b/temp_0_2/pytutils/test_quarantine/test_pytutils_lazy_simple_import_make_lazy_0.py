
# Module: pytutils.lazy.simple_import
# test_lazy_import.py
from unittest import mock
import pytest
import sys
from types import ModuleType
from pytutils.lazy.simple_import import make_lazy, NonLocal

@pytest.fixture(autouse=True)
def reset_sys_modules():
    """Reset sys.modules before each test to ensure no module is cached."""
    yield
    if 'math' in sys.modules:
        del sys.modules['math']

def test_basic_usage():
    lm = make_lazy('math')
    assert hasattr(lm, 'sqrt'), "The math module should be imported when accessing sqrt."
    assert lm.sqrt(16) == 4.0, "Calling sqrt on the lazily imported math module should return the correct value."

def test_accessing_non_existent_attribute():
    lm = make_lazy('math')
    with pytest.raises(AttributeError):
        lm.does_not_exist  # Accessing a non-existent attribute should raise an AttributeError.

@mock.patch('sys.modules', {})
def test_handling_module_not_found():
    with pytest.raises(ImportError):
        make_lazy('non_existent_module')  # Attempting to import a non-existent module should raise ImportError.

def test_using_with_another_module():
    lm = make_lazy('os')
    assert hasattr(lm, 'path'), "The os module should be imported when accessing path."
    assert lm.path.join('/usr', 'local') == '/usr/local', "Calling join on the lazily imported os.path should return the correct value."

def test_using_with_builtin_module():
    lm = make_lazy('sys')
    assert hasattr(lm, 'modules'), "The sys module should be imported when accessing modules."
    assert isinstance(lm.modules, dict), "The modules attribute of the lazily imported sys module should be a dictionary."

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_make_lazy_0
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0.py:18:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0.py:23:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0.py:33:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0.py:38:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""
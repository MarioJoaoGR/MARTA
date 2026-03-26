
import pytest
from pytutils.lazy.simple_import import LazyModule

def test_invalid_input():
    with pytest.raises(AttributeError):
        lazy_module = LazyModule('non_existent_module')
        lazy_module.some_attribute  # Accessing an attribute that doesn't exist should raise AttributeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_LazyModule___getattribute___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_LazyModule___getattribute___0_test_invalid_input.py:3:0: E0611: No name 'LazyModule' in module 'pytutils.lazy.simple_import' (no-name-in-module)


"""
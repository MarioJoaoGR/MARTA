
from pytutils.lazy.simple_import import LazyModule
from types import ModuleType
import pytest

def test_valid_case():
    lazy_module = LazyModule()
    assert isinstance(lazy_module, ModuleType)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_LazyModule___mro___0_test_valid_case
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_LazyModule___mro___0_test_valid_case.py:2:0: E0611: No name 'LazyModule' in module 'pytutils.lazy.simple_import' (no-name-in-module)


"""
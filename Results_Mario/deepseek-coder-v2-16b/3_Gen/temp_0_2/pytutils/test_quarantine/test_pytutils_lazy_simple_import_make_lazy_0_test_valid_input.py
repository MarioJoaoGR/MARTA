
from pytutils.lazy.simple_import import make_lazy
import pytest
from types import ModuleType
import sys

@pytest.mark.parametrize("module_path", ["math"])
def test_valid_input(module_path):
    lazy_module = make_lazy(module_path)
    assert isinstance(lazy_module, ModuleType), "The result should be a module type."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_make_lazy_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_valid_input.py:9:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""
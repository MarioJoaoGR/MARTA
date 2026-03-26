
# Module: pytutils.lazy.simple_import
# test_lazy_module.py
from pytutils.lazy.simple_import import LazyModule
import pytest
import sys
from types import ModuleType
from unittest.mock import patch

@pytest.fixture
def lazy_math():
    return LazyModule('math')

@pytest.fixture
def mock_math_module():
    math_module = ModuleType('math')
    math_module.sqrt = lambda x: x**0.5
    sys.modules['math'] = math_module
    yield math_module
    del sys.modules['math']

def test_lazy_import(mock_math_module, lazy_math):
    with patch('builtins.__import__', side_effect=lambda name, globals=None, locals=None, fromlist=None: mock_math_module):
        assert lazy_math.sqrt(4) == 2.0

def test_lazy_import_multiple_calls(mock_math_module, lazy_math):
    with patch('builtins.__import__', side_effect=lambda name, globals=None, locals=None, fromlist=None: mock_math_module):
        assert lazy_math.sqrt(4) == 2.0
        assert lazy_math.sqrt(9) == 3.0

def test_lazy_import_not_existing_attribute():
    lazy_module = LazyModule('math')
    with pytest.raises(AttributeError):
        getattr(lazy_module, 'does_not_exist')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_LazyModule___getattribute___0
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_LazyModule___getattribute___0.py:4:0: E0611: No name 'LazyModule' in module 'pytutils.lazy.simple_import' (no-name-in-module)


"""
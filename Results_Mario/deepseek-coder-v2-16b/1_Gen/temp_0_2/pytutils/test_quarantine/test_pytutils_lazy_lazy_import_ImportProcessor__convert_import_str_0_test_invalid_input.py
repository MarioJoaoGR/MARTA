
import pytest
from pytutils.lazy import ImportProcessor

def test_invalid_input():
    processor = ImportProcessor()
    with pytest.raises(ValueError):
        processor._convert_import_str('import foo, foo.bar, foo.bar.baz as bing')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_0_test_invalid_input.py:3:0: E0611: No name 'ImportProcessor' in module 'pytutils.lazy' (no-name-in-module)


"""
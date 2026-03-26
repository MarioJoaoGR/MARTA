
from pytutils.lazy import lazy_import
from pytutils.lazy.lazy_import import ImportReplacer

def test_edge_case_none():
    processor = ImportProcessor()
    assert isinstance(processor._lazy_import_class, ImportReplacer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__build_map_0_test_edge_case_none
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__build_map_0_test_edge_case_none.py:6:16: E0602: Undefined variable 'ImportProcessor' (undefined-variable)


"""

import pytest
from pytutils.sets import MetaSet

def test_edge_cases():
    # Test with None initial value
    meta_set = MetaSet(initial=None)
    assert len(meta_set._store) == 0
    assert meta_set._initial is None
    
    # Test with empty set initial value
    meta_set = MetaSet(initial=[])
    assert len(meta_set._store) == 0
    assert meta_set._initial == []
    
    # Test with non-empty set initial value
    meta_set = MetaSet(initial=[1, 2, 3])
    assert list(meta_set._store) == [1, 2, 3]
    assert meta_set._initial == [1, 2, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___iter___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None initial value
        meta_set = MetaSet(initial=None)
        assert len(meta_set._store) == 0
        assert meta_set._initial is None
    
        # Test with empty set initial value
        meta_set = MetaSet(initial=[])
        assert len(meta_set._store) == 0
        assert meta_set._initial == []
    
        # Test with non-empty set initial value
        meta_set = MetaSet(initial=[1, 2, 3])
        assert list(meta_set._store) == [1, 2, 3]
>       assert meta_set._initial == [1, 2, 3]
E       AttributeError: 'MetaSet' object has no attribute '_initial'

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___iter___1_test_edge_cases.py:19: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___iter___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.06s ===============================
"""
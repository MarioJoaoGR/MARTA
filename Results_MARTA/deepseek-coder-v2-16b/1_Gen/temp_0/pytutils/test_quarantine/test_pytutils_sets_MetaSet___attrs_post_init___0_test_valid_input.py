
import pytest
from pytutils.sets import MetaSet
from datetime import datetime

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    lst = [1, 2, 3, 4]
    meta_set.update(lst)
    
    assert len(meta_set._store) == 4
    for item in lst:
        assert item in meta_set._store
        assert 'added_at' in meta_set._meta[item]

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

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___attrs_post_init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

meta_set = MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f0cb351dd00>, _store={1, 2, 3, 4}, _meta={1: 0, 2: 1, 3: 0, 4: 1}, _initial=None)

    def test_valid_input(meta_set):
        lst = [1, 2, 3, 4]
        meta_set.update(lst)
    
        assert len(meta_set._store) == 4
        for item in lst:
            assert item in meta_set._store
>           assert 'added_at' in meta_set._meta[item]
E           TypeError: argument of type 'int' is not iterable

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___attrs_post_init___0_test_valid_input.py:17: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___attrs_post_init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""